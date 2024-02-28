import datetime
import os
import django
import math
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WBTBSsystem.settings')
django.setup()
from system.models import ContainerBoat, Task, Berth, ScheduleEntry
import pandas as pd

def getData():
    ScheduleEntryList=ScheduleEntry.objects.all()
    return ScheduleEntryList

def DataTOExcel():
    ScheduleEntryList=getData()
    data = []
    for i in range(len(ScheduleEntryList)):
        data.append([ScheduleEntryList[i].TaskId.ContainerBoatID.ContainerBoatID, ScheduleEntryList[i].TaskId.Action,ScheduleEntryList[i].TaskId.startTime,ScheduleEntryList[i].TaskId.endTime,ScheduleEntryList[i].listOfTugBoats,ScheduleEntryList[i].State])
    df = pd.DataFrame(data, columns=['ContainerBoatID','Action','startTime','endTime','listOfTugBoats','State'])
    df.to_excel('web\WBTBSsystem\\testOut.xlsx', index=False)
    return

def main():
    DataTOExcel()
    return

if __name__ == '__main__':
    main()