import sqlite3
import datetime
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

def AutoSchedule_taskTOschedule():
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    for task in TaskList:
        if task.State == 'Scheduled':
            continue
        if task.startTime > datetime.datetime.now().replace(tzinfo=pytz.timezone('Asia/Shanghai')):
            schedule = ScheduleEntry()
            schedule.TaskId = task
            schedule.save()
    return

def ifTugBoatAvailable(tugboat, task):
    if task.startTime < tugboat.StartWorkingTime or task.endTime > tugboat.EndWorkingTime:
        return False
    for schedule in ScheduleEntry.objects.all():
        if schedule.State == 'Scheduled':
            for boat in schedule.listOfTugBoats.all():
                if boat.TugBoatId == tugboat.TugBoatId:
                    if schedule.TaskId.startTime < task.endTime and schedule.TaskId.endTime > task.startTime:
                        return False
def AutoSchedule():
    AutoSchedule_taskTOschedule()
    TugBoatList = TugBoat.objects.all()
    ScheduleEntryList = ScheduleEntry.objects.all()
    for schedule in ScheduleEntryList:
        if schedule.State == 'Scheduled':
            continue
        for tugboat in TugBoatList:
            for i in range(schedule.TaskId.ReqauriedTugBoat):
                if ifTugBoatAvailable(tugboat, schedule.TaskId):
                    schedule.listOfTugBoats.add(tugboat)
                    tugboat.CurrentStatus = 'Busy'
                    tugboat.save()
                    schedule.State = 'Scheduled'
                    schedule.save()
    AutoSchedule_Complete()
    return



if __name__ == '__main__':
    AutoSchedule()
    print('AutoSchedule Finished')
    print('ScheduleEntry:')
    for schedule in ScheduleEntry.objects.all():
        print(schedule.TaskId.TaskId, schedule.State)