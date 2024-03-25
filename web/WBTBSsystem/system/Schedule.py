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
from system.models import Captain, TugBoat, ContainerBoat, Task, ScheduleEntry, User, Berth

def Get_Information(): # Get all the information from the database
    TaskList=Task.objects.all().order_by('startTime')
    TugBoatList=TugBoat.objects.all()
    ScheduleEntryList=ScheduleEntry.objects.all()
    return TaskList, TugBoatList, ScheduleEntryList

def AutoSchedule_ScheduleEntry_Complete(): # Check if the schedule entry is completed
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    for schedule in ScheduleEntryList:
        if schedule.EndTime==None:
            continue
        if schedule.EndTime.date() <= datetime.datetime.now().date()-datetime.timedelta(days=1):
            schedule.Status = 'Completed'
            schedule.save()

def AutoSchedule_Reschedule(): # Reschedule the task
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    print("reschedule 1")
    for schedule in ScheduleEntryList:
        print(schedule.TaskId.TaskId, schedule.Status)
        if schedule.TaskId.TaskManual == 1:
            continue
        if schedule.Status=='Scheduled':
            schedule.TaskId.State = 'Unscheduled'
            schedule.TaskId.save()
            schedule.delete()
    print("reschedule 2")
    AutoSchedule()

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
                        if schedule.TaskId.TaskId != task.TaskId:
                            return False
    return True
def IsberthAvailable(berthID):
    # Determine if the berth is available
    try:
        berth=Berth.objects.get(BerthId=berthID)
    except:
        return False
    if berth.ContainerBoat==None:
        return True
    else:
        return False
def AutoSchedule_NextFit():# Auto Schedule the task--->ScheduleEntry (next fit)
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    AutoSchedule_task_Complete()
    index = 0
    for task in TaskList:
        if IsberthAvailable(task.BerthId) == False:
            continue
        if task.TaskManual == 1:
            continue
        if task.State == 'Unscheduled' and (task.startTime.date() == datetime.datetime.now().date() or task.startTime.date()== datetime.datetime.now().date()+datetime.timedelta(days=1))  and task.startTime > datetime.datetime.now():
            schedule = ScheduleEntry(TaskId=task, Status='Scheduled', StartTime=None, EndTime=None)
            schedule.save()
            n=0
            count = 0
            while n < task.RequiredTugBoat:
                if ifTugBoatAvailable(TugBoatList[index], task):
                    schedule.listOfTugBoats.add(TugBoatList[index])
                    n+=1
                    if(n==task.RequiredTugBoat):
                        break
                index = (index+1)%len(TugBoatList)
                if(index>=len(TugBoatList)):
                    index = 0
                count += 1
                if count == len(TugBoatList):
                    break
            print("nextfit")
            if n < task.RequiredTugBoat:
                task.State = 'Unscheduled'
                print('No enough tugboat available')
                schedule.delete()
                task.save()
                return (True, "Scheduling completed successfully.")
            task.State = 'Scheduled'
            schedule.save()
            task.save()
    return (True, "Scheduling completed successfully.")
def AutoSchedule_FIFO(): # Auto Schedule the task--->ScheduleEntry (first come first serve)
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    AutoSchedule_task_Complete() 
    for task in TaskList:
        if IsberthAvailable(task.BerthId) == False:
            continue
        if task.TaskManual == 1:
            continue
        if task.State == 'Unscheduled' and (task.startTime.date() == datetime.datetime.now().date() or task.startTime.date()== datetime.datetime.now().date()+datetime.timedelta(days=1))  and task.startTime > datetime.datetime.now():
            schedule = ScheduleEntry(TaskId=task, Status='Scheduled', StartTime=None, EndTime=None)
            schedule.save()
            n=0
            for tugboat in TugBoatList:
                if ifTugBoatAvailable(tugboat, task):
                    print(tugboat.TugBoatId)
                    schedule.listOfTugBoats.add(tugboat)
                    n+=1
                    if(n==task.RequiredTugBoat):
                        break
            print("autooo")
            if n < task.RequiredTugBoat:
                task.State = 'Unscheduled'
                print('No enough tugboat available')
                schedule.delete()
                task.save()
                return
            task.State = 'Scheduled'
            schedule.save()
            task.save()

    return (True, "Scheduling completed successfully.")

def AutoSchedule():
    tasklist = Task.objects.all()
    totalTugBoatNeeded = 0
    for task in tasklist:
        if task.State == 'Unscheduled':
            totalTugBoatNeeded += task.RequiredTugBoat
    tugboatlist = TugBoat.objects.all()
    totalTugBoatAvailable = 0
    for boat in tugboatlist:
        if boat.CurrentStatus != 'Maintenance':
            totalTugBoatAvailable += 1
    if totalTugBoatNeeded > totalTugBoatAvailable:
        return AutoSchedule_NextFit()
    else:
        return AutoSchedule_FIFO()

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