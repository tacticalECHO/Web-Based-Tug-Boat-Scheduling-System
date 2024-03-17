from datetime import *
import pytest
import os
import time
import django
import sys
sys.path.append('web\\WBTBSsystem')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WBTBSsystem.settings')
django.setup()
from system.models import ContainerBoat, Task, Berth, TugBoat, Captain
from system.Schedule import *

def test_Get_Information():
    Task.objects.all().delete()
    TugBoat.objects.all().delete()
    ScheduleEntry.objects.all().delete()
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    assert len(TaskList) == 0
    assert len(TugBoatList) == 0
    assert len(ScheduleEntryList) == 0
    ContainerBoat.objects.create(ContainerBoatID="CB123", Tonnage=1000, Country="Country X")
    TugBoat.objects.create(TugBoatId="TB123")
    Task.objects.create(ContainerBoatID=ContainerBoat.objects.get(ContainerBoatID="CB123"), RequiredTugBoat=1, startTime=datetime.datetime.now(), Action='INBOUND')
    ScheduleEntry.objects.create(TaskId=Task.objects.get(ContainerBoatID=ContainerBoat.objects.get(ContainerBoatID="CB123")))
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    assert len(TaskList) == 1
    assert len(TugBoatList) == 1
    assert len(ScheduleEntryList) == 1

def test_AutoSchedule_ScheduleEntry_Complete():
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    AutoSchedule_ScheduleEntry_Complete()
    assert ScheduleEntryList[0].Status == 'Scheduled'
    Schedule=ScheduleEntryList[0]
    Schedule.EndTime=datetime.datetime.now()-datetime.timedelta(days=2)
    Schedule.save()
    Schedule.StartTime=datetime.datetime.now()-datetime.timedelta(days=3)
    Schedule.save()
    AutoSchedule_ScheduleEntry_Complete()
    assert ScheduleEntryList[0].Status == 'Completed'

def test_task_Complete():
    TaskList, TugBoatList, ScheduleEntryList = Get_Information()
    Task=TaskList[0]
    Task.State='Scheduled'
    Task.save()
    Task.startTime=datetime.datetime.now()-datetime.timedelta(days=2)
    Task.save()
    AutoSchedule_task_Complete()
    assert TaskList[0].State == 'Completed'
    Task=TaskList[0]
    Task.State='Unscheduled'
    Task.save()
    Task.startTime=datetime.datetime.now()-datetime.timedelta(days=2)
    Task.save()
    AutoSchedule_task_Complete()
    assert TaskList[0].State == 'Expired'

def test_ifTugBoatAvailable():
    TugBoat.objects.create(TugBoatId="TB124", CurrentStatus='Maintenance', StartWorkingTime=datetime.time(0, 0), EndWorkingTime=datetime.time(23, 59))
    Task_test=Task.objects.get(ContainerBoatID=ContainerBoat.objects.get(ContainerBoatID="CB123"), RequiredTugBoat=1, Action='INBOUND')
    TugBoat_test=TugBoat.objects.get(TugBoatId="TB123")
    assert ifTugBoatAvailable(TugBoat_test, Task_test) == False
    TugBoat_test.CurrentStatus='Available'
    TugBoat_test.save()
    assert ifTugBoatAvailable(TugBoat_test, Task_test) == False
    TugBoat_test.StartWorkingTime=datetime.time(0, 0)
    TugBoat_test.save()
    TugBoat_test.EndWorkingTime=datetime.time(23, 59)
    TugBoat_test.save()
    assert ifTugBoatAvailable(TugBoat_test, Task_test) == True
    TugBoat_test.CurrentStatus='Busy'

def test_AutoSchedule_NextFit():
    ContainerBoat.objects.create(ContainerBoatID="CB125", Tonnage=1000, Country="Country X")
    Task.objects.create(ContainerBoatID=ContainerBoat.objects.get(ContainerBoatID="CB125"), RequiredTugBoat=1, startTime=datetime.datetime.now()+timedelta(hours=1), Action='INBOUND',BerthId=1)
    AutoSchedule_NextFit()
    ScheduleCB125=ScheduleEntry.objects.get(TaskId=Task.objects.get(ContainerBoatID=ContainerBoat.objects.get(ContainerBoatID="CB125")))
    assert ScheduleCB125.Status == 'Scheduled'
    assert ScheduleCB125.listOfTugBoats.all()[0].TugBoatId == 'TB123'
    TugBoat.objects.create(TugBoatId="TB125", CurrentStatus='Maintenance', StartWorkingTime=datetime.time(0, 0), EndWorkingTime=datetime.time(23, 59))
    

def test_AutoSchedule_Reschedule():
    AutoSchedule_Reschedule()
    ScheduleEn=ScheduleEntry.objects.get(TaskId=Task.objects.get(ContainerBoatID=ContainerBoat.objects.get(ContainerBoatID="CB125")))
    assert ScheduleEn.listOfTugBoats.all()[0].TugBoatId == 'TB123'

def test_AutoSchedule_FIFO():
    Task.objects.all().delete()
    ScheduleEntry.objects.all().delete()
    ContainerBoat.objects.create(ContainerBoatID="CB126", Tonnage=1000, Country="Country X")
    Task.objects.create(ContainerBoatID=ContainerBoat.objects.get(ContainerBoatID="CB126"), RequiredTugBoat=1, startTime=datetime.datetime.now()+timedelta(hours=1), Action='INBOUND',BerthId=10)
    AutoSchedule_FIFO()
    ScheduleCB126=ScheduleEntry.objects.get(TaskId=Task.objects.get(ContainerBoatID=ContainerBoat.objects.get(ContainerBoatID="CB126")))
    assert ScheduleCB126.Status == 'Scheduled'
    assert ScheduleCB126.listOfTugBoats.all()[0].TugBoatId == 'TB123'