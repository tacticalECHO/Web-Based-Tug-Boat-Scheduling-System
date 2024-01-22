import sqlite3
import datetime
import pytz
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WBTBSsystem.settings')
django.setup()
from system.models import Captain, TugBoat, ContainerBoat, Task, ScheduleEntry, User

def Get_Information():
    TaskList=Task.objects.all().order_by('startTime')
    TugBoatList=TugBoat.objects.all()
    ScheduleEntryList=ScheduleEntry.objects.all()
    return TaskList, TugBoatList, ScheduleEntryList

def AutoSchedule():
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    print(ScheduleEntryList)
    for task in TaskList:
        i=0
        if task.State == 'Scheduled':
            continue
        if task.Action == 'Arrival':
            if task.startTime > datetime.datetime.now().replace(tzinfo=pytz.timezone('Asia/Shanghai')):
                schedule = ScheduleEntry()
                schedule.TaskId = task
                schedule.State = 'Scheduled'
                schedule.save()
                for tugboat in TugBoatList:
                    if(i==task.ReqauriedTugBoat):
                        break
                    if tugboat.CurrentStatus == 'Free':
                        tugboat.CurrentStatus = 'Busy'
                        tugboat.save()
                        schedule.listOfTugBoats.add(tugboat)
                        schedule.save()
                        i+=1
                        
                task.State = 'Scheduled'
                task.save()
                break
        elif task.Action == 'Departure':
            if task.startTime > datetime.datetime.now().replace(tzinfo=pytz.timezone('Asia/Shanghai')):
                for tugboat in TugBoatList:
                    if tugboat.CurrentStatus == 'Free':
                        tugboat.CurrentStatus = 'Busy'
                        tugboat.save()
                        schedule = ScheduleEntry()
                        schedule.TaskId = task
                        schedule.State = 'Scheduled'
                        schedule.save()
                        schedule.listOfTugBoats.add(tugboat)
                        schedule.save()
                        task.State = 'Scheduled'
                        task.save()
                        break
        
    for schedule in ScheduleEntryList:
        if schedule.State == 'Scheduled':
            if schedule.TaskId.endTime < datetime.datetime.now().replace(tzinfo=pytz.timezone('Asia/Shanghai')):
                schedule.State = 'Completed'
                schedule.save()
                for tugboat in schedule.listOfTugBoats.all():
                    tugboat.CurrentStatus = 'Free'
                    tugboat.save()
                schedule.listOfTugBoats.clear()
                schedule.save()
    return

if __name__ == '__main__':
    AutoSchedule()
    print('AutoSchedule Finished')
    print('ScheduleEntry:')
    for schedule in ScheduleEntry.objects.all():
        print(schedule.TaskId.TaskId, schedule.State)