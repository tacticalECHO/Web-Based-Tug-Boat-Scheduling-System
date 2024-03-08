import sqlite3
import datetime
import time
import pytz
import os
import django
import sys
sys.path.append('web\WBTBSsystem')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WBTBSsystem.settings')
django.setup()
from system.models import Captain, TugBoat, ContainerBoat, Task, ScheduleEntry, User

def Get_Information(): # Get all the information from the database
    TaskList=Task.objects.all().order_by('startTime')
    TugBoatList=TugBoat.objects.all()
    ScheduleEntryList=ScheduleEntry.objects.all()
    return TaskList, TugBoatList, ScheduleEntryList


def AutoSchedule_task_Complete(): # Check if the task is completed
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    for task in TaskList:
        if task.State == 'Scheduled':
            if task.startTime.date() <= datetime.datetime.now().date()-datetime.timedelta(days=1):
                task.State = 'Completed'
                task.save()
        elif task.State == 'Unscheduled':
            if task.startTime.date() < datetime.datetime.now().date():
                task.State = 'Expired'
                task.save()

def ifTugBoatAvailable(tugboat, task): # Check if the tugboat is available at the task time
    StartTime = task.startTime-datetime.timedelta(hours=1)
    EndTime = task.startTime+datetime.timedelta(hours=1)
    if tugboat.CurrentStatus =='Maintenance':
        return False
    if StartTime.time()< tugboat.StartWorkingTime or EndTime.time() > tugboat.EndWorkingTime:
        return False
    for schedule in ScheduleEntry.objects.all():
        if schedule.Status == 'Scheduled':
            for boat in schedule.listOfTugBoats.all():
                if boat.TugBoatId == tugboat.TugBoatId:
                    if schedule.TaskId.startTime-datetime.timedelta(hours=1) < EndTime and schedule.TaskId.startTime+datetime.timedelta(hours=1) > StartTime:
                        return False
    return True
def AutoSchedule(): # Auto Schedule the task--->ScheduleEntry (first come first serve)
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    AutoSchedule_task_Complete() 
    for task in TaskList:
        if task.State == 'Unscheduled' and (task.startTime.date() == datetime.datetime.now().date() or task.startTime.date()== datetime.datetime.now().date()+datetime.timedelta(days=1))  and task.startTime > datetime.datetime.now():
            ST=task.startTime-datetime.timedelta(hours=1)
            ET=task.startTime+datetime.timedelta(hours=1)
            schedule = ScheduleEntry(TaskId=task, Status='Scheduled', PublishTime=datetime.datetime.now(), StartTime=ST, EndTime=ET)
            schedule.save()
            n=0
            for tugboat in TugBoatList:
                if ifTugBoatAvailable(tugboat, task):
                    print(tugboat.TugBoatId)
                    schedule.listOfTugBoats.add(tugboat)
                    n+=1
                    if(n==task.RequiredTugBoat):
                        break
            task.State = 'Scheduled'
            if n < task.RequiredTugBoat:
                task.State = 'Unscheduled'
                print('No enough tugboat available')
                schedule.delete()
                task.save()
                return
            schedule.save()
            task.save()

    return (True, "Scheduling completed successfully.")



if __name__ == '__main__':
    AutoSchedule()
    print('AutoSchedule Finished')
    print('ScheduleEntry:')
    for schedule in ScheduleEntry.objects.all():
        print(schedule.TaskId.TaskId, schedule.Status)
        for boat in schedule.listOfTugBoats.all():
            print(boat.TugBoatId, boat.CurrentStatus)
    print('TugBoat:')
    for boat in TugBoat.objects.all():
        print(boat.TugBoatId, boat.CurrentStatus)