import sqlite3
import datetime
import time
import pytz
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WBTBSsystem.settings')
django.setup()
from system.models import Captain, TugBoat, ContainerBoat, Task, ScheduleEntry, User

def Get_Information(): # Get all the information from the database
    TaskList=Task.objects.all().order_by('startTime')
    TugBoatList=TugBoat.objects.all()
    ScheduleEntryList=ScheduleEntry.objects.all()
    return TaskList, TugBoatList, ScheduleEntryList

def AutoSchedule_Complete(): # Check if the task is completed
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    for schedule in ScheduleEntryList:
        if schedule.State == 'Scheduled':
            if schedule.TaskId.startTime < datetime.datetime.now().replace(tzinfo=pytz.timezone('Asia/Shanghai')):
                schedule.State = 'Completed'
                schedule.save()
                for tugboat in schedule.listOfTugBoats.all():
                    tugboat.CurrentStatus = 'Free'
                    tugboat.save()
                schedule.listOfTugBoats.clear()
                schedule.save()
    return


def ifTugBoatAvailable(tugboat, task):
    StartTime = task.startTime.time()
    EndTime = task.endTime.time()
    if StartTime< tugboat.StartWorkingTime or EndTime > tugboat.EndWorkingTime:
        return False
    for schedule in ScheduleEntry.objects.all():
        if schedule.State == 'Scheduled':
            for boat in schedule.listOfTugBoats.all():
                if boat.TugBoatId == tugboat.TugBoatId:
                    if schedule.TaskId.startTime < task.endTime and schedule.TaskId.endTime > task.startTime:
                        return False
    return True
def AutoSchedule():
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    AutoSchedule_Complete()
    for task in TaskList:
        if task.State == 'Unscheduled':
            schedule = ScheduleEntry(TaskId=task, State='Scheduled')
            schedule.save()
            for i in range(task.ReqauriedTugBoat):
                n=0
                for tugboat in TugBoatList:
                    if ifTugBoatAvailable(tugboat, task):
                        schedule.listOfTugBoats.add(tugboat)
                        tugboat.CurrentStatus = 'Busy'
                        n+=1
                        break
            task.State = 'Scheduled'
            tugboat.save()
            if n < task.ReqauriedTugBoat:
                task.State = 'Unscheduled'
                schedule.delete()
                task.save()
                return
            schedule.save()
            task.save()

    return



if __name__ == '__main__':
    AutoSchedule()
    print('AutoSchedule Finished')
    print('ScheduleEntry:')
    for schedule in ScheduleEntry.objects.all():
        print(schedule.TaskId.TaskId, schedule.State)
        for boat in schedule.listOfTugBoats.all():
            print(boat.TugBoatId)
    print('TugBoat:')
    for boat in TugBoat.objects.all():
        print(boat.TugBoatId, boat.CurrentStatus)