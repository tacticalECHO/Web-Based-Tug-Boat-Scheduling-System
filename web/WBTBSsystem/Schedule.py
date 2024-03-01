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
            if schedule.TaskId.startTime < datetime.datetime.now():
                schedule.State = 'Completed'
                schedule.save()
                schedule.TaskId.State = 'Completed'
                schedule.save()
                schedule.TaskId.save()
            if schedule.TaskId.endTime.date() <= datetime.datetime.now().date()-datetime.timedelta(days=1):
                schedule.delete()
                
    return

def AutoSchedule_task_Complete(): # Check if the task is completed
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    for task in TaskList:
        if task.State == 'Scheduled':
            if task.endTime.date() <= datetime.datetime.now().date()-datetime.timedelta(days=1):
                task.State = 'Completed'
                task.save()
        elif task.State == 'Unscheduled':
            if task.startTime.date() < datetime.datetime.now().date():
                task.State = 'Expired'
                task.save()

def ifTugBoatAvailable(tugboat, task): # Check if the tugboat is available at the task time
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
def AutoSchedule(): # Auto Schedule the task--->ScheduleEntry (first come first serve)
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    AutoSchedule_task_Complete() 
    AutoSchedule_Complete()
    for task in TaskList:
        if task.State == 'Unscheduled' and task.startTime.date() == datetime.datetime.now().date():
            schedule = ScheduleEntry(TaskId=task, State='Scheduled')
            schedule.save()
            for i in range(task.RequiredTugBoat):
                n=0
                for tugboat in TugBoatList:
                    if ifTugBoatAvailable(tugboat, task):
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

    return



if __name__ == '__main__':
    AutoSchedule()
    print('AutoSchedule Finished')
    print('ScheduleEntry:')
    for schedule in ScheduleEntry.objects.all():
        print(schedule.TaskId.TaskId, schedule.State)
        for boat in schedule.listOfTugBoats.all():
            print(boat.TugBoatId, boat.CurrentStatus)
    print('TugBoat:')
    for boat in TugBoat.objects.all():
        print(boat.TugBoatId, boat.CurrentStatus)