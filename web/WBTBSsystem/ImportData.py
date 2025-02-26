import datetime
import os
import django
import math
import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WBTBSsystem.settings')
django.setup()
from system.models import ContainerBoat, Task
import pandas as pd
import numpy as np
path="test.xlsx"
hash_berth = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: []
}
def WhichberthAvailable(arrivalTime, departureTime):
    # Check if the berth is available
    for key, value in hash_berth.items():
        if len(value) == 0:
            return key
        else:
            for i in range(len(value)):
                if arrivalTime > value[i][1] or departureTime < value[i][0]:
                    return key
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
def WhetherArrOrDep(data):
    ArrivalList=[]
    DepartureList=[]
    # Determine if the task is an arrival or departure task
    for i in range(len(data)):
        if str_to_date(data.iloc[i,3])==datetime.date.today() or str_to_date(data.iloc[i,3])==datetime.date.today()+datetime.timedelta(days=1):
            ArrivalList.append(i)
        if str_to_date(data.iloc[i,4])==datetime.date.today() or str_to_date(data.iloc[i,4])==datetime.date.today()+datetime.timedelta(days=1):
            DepartureList.append(i)
    return ArrivalList,DepartureList

def createTask(data):
    # Create tasksw
    ArrivalList,DepartureList=WhetherArrOrDep(data)
    print(ArrivalList)
    for i in ArrivalList:
        berth=WhichberthAvailable(data.iloc[i,3],data.iloc[i,4])
        if(berth!=-1):
            Task.objects.create(ReqauriedTugBoat=requieredTugBoat(data.iloc[i,1]),startTime=data.iloc[i,3]-datetime.timedelta(hours=1),endTime=data.iloc[i,3]+datetime.timedelta(hours=1),ContainerBoatID=ContainerBoat.objects.get(ContainerBoatID=data.iloc[i,0]),Action='Arrival',BerthId=berth,State='Unscheduled')
            hash_berth[berth].append([data.iloc[i,3],data.iloc[i,4]])
    for i in DepartureList:
        for key, value in hash_berth.items():
            for j in range(len(value)):
                if data.iloc[i,3]==value[j][0] and data.iloc[i,4] ==value[j][1]:
                    Task.objects.create(ReqauriedTugBoat=requieredTugBoat(data.iloc[i,1]),startTime=data.iloc[i,3]-datetime.timedelta(hours=1),endTime=data.iloc[i,3]+datetime.timedelta(hours=1),ContainerBoatID=ContainerBoat.objects.get(ContainerBoatID=data.iloc[i,0]),Action='Departure',BerthId=key,State='Unscheduled')
                    break
if __name__ == "__main__":
    
    data=importData()
    dataIntoDatabase(data)
    createTask(data)
    print(data)