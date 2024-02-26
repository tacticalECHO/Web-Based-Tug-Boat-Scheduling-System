import datetime
import os
import django
import math
import time

import pytz
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WBTBSsystem.settings')
django.setup()
from system.models import ContainerBoat, Task, Berth
import pandas as pd
import numpy as np
path="web\WBTBSsystem\\test.xlsx"

def WhichberthAvailable(arrivalTime, departureTime):
    # Determine which berth is available
    berthList=Berth.objects.all()
    for i in range(len(berthList)):
        if berthList[i].ContainerBoat==None:
            return berthList[i].BerthId
        if datetime.datetime.now().replace(tzinfo=pytz.timezone('Asia/Shanghai'))>berthList[i].ContainerBoat.departureTime:
            berthList[i].ContainerBoat=None
            berthList[i].save()
            return berthList[i].BerthId
    return -1
def requieredTugBoat(Tonnage):
    return math.ceil(Tonnage/1000)
def importData():
    # Import data from the xlsx file
    data = pd.read_excel(path, header=None)
    data=data.iloc[1:,:]
    df=pd.DataFrame(data)
    df.columns=['ContainerBoatID','Tonnage','Country','arrivalTime','departureTime']
    return df
def str_to_date(str):
    # Convert string to date
    Date=datetime.datetime.strptime(str, '%Y-%m-%d %H:%M')
    return Date.date()
def ifrepeat(data):
    # Determine if the data is repeated
    ContainerBoatlist=ContainerBoat.objects.all()
    for i in range(len(data)):
        for j in range(len(ContainerBoatlist)):
            if data.iloc[i,0]==ContainerBoatlist[j].ContainerBoatID:
                return True

    return False
def dataIntoDatabase(data):
    
    # Import data into the database
    for i in range(len(data)):
        if ifrepeat(data)==False:
            ContainerBoat.objects.create(ContainerBoatID=data.iloc[i,0],Tonnage=data.iloc[i,1],Country=data.iloc[i,2],arrivalTime=data.iloc[i,3],departureTime=data.iloc[i,4])
def createTask():
    # Create task
    ContainerBoatlist=ContainerBoat.objects.all()
    ContainerBoatlist=ContainerBoatlist.order_by('arrivalTime')
    for CB in ContainerBoatlist:
        BerthId=WhichberthAvailable(CB.arrivalTime,CB.departureTime)
        if BerthId!=-1:
            Task.objects.create(ReqauriedTugBoat=requieredTugBoat(CB.Tonnage),startTime=CB.arrivalTime-datetime.timedelta(minutes=30),endTime=CB.arrivalTime+datetime.timedelta(minutes=30),ContainerBoatID=CB,Action='Arrival',BerthId=BerthId,State='Unscheduled')
            Task.objects.create(ReqauriedTugBoat=requieredTugBoat(CB.Tonnage),startTime=CB.departureTime-datetime.timedelta(minutes=30),endTime=CB.departureTime+datetime.timedelta(minutes=30),ContainerBoatID=CB,Action='Departure',BerthId=BerthId,State='Unscheduled')
            berth=Berth.objects.get(BerthId=BerthId)
            berth.ContainerBoat=CB
            berth.save()
    return
if __name__ == "__main__":
    
    data=importData()
    dataIntoDatabase(data)
    createTask()
    print(data)