import datetime
import os
import django
import math
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WBTBSsystem.settings')
django.setup()
from system.models import ContainerBoat, Task, Berth
import pandas as pd
PATH="web\WBTBSsystem\\test.xlsx"

def WhichberthAvailable(arrivalTime, departureTime):
    # Determine which berth is available
    berthList=Berth.objects.all()
    for i in range(len(berthList)):
        if berthList[i].ContainerBoat==None:
            return berthList[i].BerthId
        if datetime.datetime.now()>berthList[i].ContainerBoat.departureTime:
            berthList[i].ContainerBoat=None
            berthList[i].save()
            return berthList[i].BerthId
    return -1
def requieredTugBoat(Tonnage):
    return math.ceil(Tonnage/1000)
def importData(path):
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
    for j in range(len(ContainerBoatlist)):
        if data.iloc[0]==ContainerBoatlist[j].ContainerBoatID:
            if data.iloc[3]==ContainerBoatlist[j].arrivalTime and data.iloc[4]==ContainerBoatlist[j].departureTime:
                return True

    return False
def dataIntoDatabase(data):
    
    # Import data into the database
    for i in range(len(data)):
        if ifrepeat(data.iloc[i,:])==False:
            ContainerBoat.objects.create(ContainerBoatID=data.iloc[i,0],Tonnage=data.iloc[i,1],Country=data.iloc[i,2],arrivalTime=data.iloc[i,3],departureTime=data.iloc[i,4])
def createTask():
    # Create task
    ContainerBoatlist=ContainerBoat.objects.all()
    ContainerBoatlist=ContainerBoatlist.order_by('arrivalTime')
    for CB in ContainerBoatlist:
        BerthId=WhichberthAvailable(CB.arrivalTime,CB.departureTime)
        print(BerthId)
        if BerthId!=-1:
            berth=Berth.objects.get(BerthId=BerthId)
            berth.ContainerBoat=CB
            Task.objects.create(RequiredTugBoat=requieredTugBoat(CB.Tonnage),startTime=CB.arrivalTime-datetime.timedelta(minutes=30),endTime=CB.arrivalTime+datetime.timedelta(minutes=30),ContainerBoatID=CB,Action='Arrival',BerthId=BerthId,State='Unscheduled')
            Task.objects.create(RequiredTugBoat=requieredTugBoat(CB.Tonnage),startTime=CB.departureTime-datetime.timedelta(minutes=30),endTime=CB.departureTime+datetime.timedelta(minutes=30),ContainerBoatID=CB,Action='Departure',BerthId=BerthId,State='Unscheduled')
            berth.save()
        else:
            print('No berth available')
    return
if __name__ == "__main__":
    
    data=importData(PATH)
    dataIntoDatabase(data)
    createTask()
    print(data)