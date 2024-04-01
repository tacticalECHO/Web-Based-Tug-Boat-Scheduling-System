"""created by Team 10, ©2024"""
import datetime
import os
import django
import math
import sys
sys.path.append('web\\WBTBSsystem')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WBTBSsystem.settings')
django.setup()
from system.models import ContainerBoat, Task, Berth, ScheduleEntry, TugBoat, Captain
import pandas as pd

def getData():
    ScheduleEntryList=ScheduleEntry.objects.all()
    return ScheduleEntryList

def getData_captain(captain_id):
    captain = Captain.objects.filter(CaptainId=captain_id).first()
    if not captain:
        return
    tugboat = TugBoat.objects.filter(CaptainId=captain).first() 
    if tugboat:
        schedule_entry_list = ScheduleEntry.objects.filter(listOfTugBoats__in=[tugboat]).distinct()
        return schedule_entry_list
    return


def DataTOExcel():
    ScheduleEntryList=getData()
    data = []
    for i in range(len(ScheduleEntryList)):
        tugboatlist=""
        for j in range(len(ScheduleEntryList[i].listOfTugBoats.all())):
            tugboatlist+=ScheduleEntryList[i].listOfTugBoats.all()[j].TugBoatId+"\n"
        data.append([ScheduleEntryList[i].TaskId.TaskId,ScheduleEntryList[i].TaskId.ContainerBoatID.ContainerBoatID,ScheduleEntryList[i].TaskId.Action,ScheduleEntryList[i].TaskId.BerthId,ScheduleEntryList[i].Status,ScheduleEntryList[i].PublishTime,ScheduleEntryList[i].StartTime,ScheduleEntryList[i].EndTime,tugboatlist])
    df = pd.DataFrame(data, columns=["TaskId","ContainerBoatID","Action","BerthId","Status","PublishTime","StartTime","EndTime","listOfTugBoats"])
    df.to_excel("system\\downloads\\testOut.xlsx",index=False)
    return

def DataToExcel_captain(captain_id):
    ScheduleEntryList = getData_captain(captain_id)
    data = []
    for schedule_entry in ScheduleEntryList:
        tugboat_list = ""
        for tugboat in schedule_entry.listOfTugBoats.all():
            tugboat_list += tugboat.TugBoatId + "\n"
        data.append([
            schedule_entry.TaskId.TaskId,
            schedule_entry.TaskId.ContainerBoatID.ContainerBoatID,
            schedule_entry.TaskId.Action,
            schedule_entry.TaskId.BerthId,
            schedule_entry.Status,
            schedule_entry.PublishTime,
            schedule_entry.StartTime,
            schedule_entry.EndTime,
            tugboat_list
        ])
    df = pd.DataFrame(data, columns=["TaskId", "ContainerBoatID", "Action", "BerthId", "Status", "PublishTime", "StartTime", "EndTime", "listOfTugBoats"])
    df.to_excel("system\\downloads\\testOut_captain.xlsx", index=False)
    return


def main():
    DataTOExcel()
    return

if __name__ == '__main__':
    main()