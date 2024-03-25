import datetime
import os
import django
import math
import sys
sys.path.append('web\WBTBSsystem')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WBTBSsystem.settings')
django.setup()
from system.models import ContainerBoat, Task, Berth, TugBoat, Captain
import pandas as pd
PATH="web\WBTBSsystem\\test_container.xlsx"

def requieredTugBoat(Tonnage):
    return math.ceil(Tonnage/1000)
def importData(path):
    # Import data from the xlsx file
    data = pd.read_excel(path, header=None)
    data=data.iloc[1:,:]
    df=pd.DataFrame(data)
    df.columns=['ContainerBoatID','Tonnage','Country','ScheduleTime','Action','BerthID']
    return df
def str_to_date(str):
    # Convert string to date
    Date=datetime.datetime.strptime(str, '%Y-%m-%d %H:%M')
    return Date.date()
def ifrepeat(data):
    # Determine if the data is repeated
    try:
        ContainerBoat.objects.get(ContainerBoatID=data.iloc[0])
        return True
    except:
        return False
def dataIntoDatabase_ContainerBoat(data):
    # Import data into the database
    for i in range(len(data)):
        if ifrepeat(data.iloc[i,:])==False:
            ContainerBoat.objects.create(ContainerBoatID=data.iloc[i,0],Tonnage=data.iloc[i,1],Country=data.iloc[i,2])
    return
def dataIntoDatabase_TugBoat(data):
    # Import TugBoat data into the database, ignore if TugBoat already exists
    for index, row in data.iterrows():
        try:
            captain = Captain.objects.get(CaptainId=row['CaptainId'])
            captain_id = captain
        except Captain.DoesNotExist:
            captain_id = None
        TugBoat.objects.create(
            TugBoatId=row['TugBoatId'],
            CurrentStatus=row['CurrentStatus'],
            CaptainId=captain_id,
            StartWorkingTime=row['StartWorkingTime'],
            EndWorkingTime=row['EndWorkingTime'],
        )
def IfTaskRepeat(data):
    # Determine if the task is repeated
    try:
        Task.objects.get(ContainerBoatID=ContainerBoat.objects.get(ContainerBoatID=data[0]),BerthId=data[5],startTime=data[3],Action=data[4])
        return True
    except:
        return False
def createTask(data):
    # Create task
    data.sort_values(by='ScheduleTime',ascending=True)
    for i in range(len(data)):
        if  IfTaskRepeat(data.iloc[i,:])==False:
            ScheduleTime=data.iloc[i,3]
            Task.objects.create(ContainerBoatID=ContainerBoat.objects.get(ContainerBoatID=data.iloc[i,0]),BerthId=data.iloc[i,5],startTime=ScheduleTime,Action=data.iloc[i,4],RequiredTugBoat=requieredTugBoat(data.iloc[i,1]))

    return
if __name__ == "__main__":
    
    data=importData(PATH)
    dataIntoDatabase_ContainerBoat(data)
    createTask(data)
    print(data)