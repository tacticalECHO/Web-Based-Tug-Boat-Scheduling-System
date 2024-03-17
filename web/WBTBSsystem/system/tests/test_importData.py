import pytest
import sys
sys.path.append('web\\WBTBSsystem')
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WBTBSsystem.settings')
django.setup()
from system.models import ContainerBoat, Task, Berth, TugBoat, Captain, ScheduleEntry
from system.ImportData import *

def test_IsberthAvailable():
    assert IsberthAvailable(1) == True
    assert IsberthAvailable(2) == True
    assert IsberthAvailable(3) == True
    assert IsberthAvailable(4) == True
    assert IsberthAvailable(5) == True
    assert IsberthAvailable(6) == True
    assert IsberthAvailable(7) == True
    assert IsberthAvailable(8) == True
    assert IsberthAvailable(9) == True
    assert IsberthAvailable(10) == True
    Berth.objects.create(BerthId=11)
    assert IsberthAvailable(11) == True
    ContainerBoat.objects.create(ContainerBoatID="CB123", Tonnage=1000, Country="Country X")
    Berth.objects.create(BerthId=12, ContainerBoat=ContainerBoat.objects.get(ContainerBoatID="CB123"))
    assert IsberthAvailable(12) == False
    Berth.delete(Berth.objects.get(BerthId=11))
    Berth.delete(Berth.objects.get(BerthId=12))
    ContainerBoat.delete(ContainerBoat.objects.get(ContainerBoatID="CB123"))

def test_requieredTugBoat():
    assert requieredTugBoat(1000) == 1
    assert requieredTugBoat(1879) == 2
    assert requieredTugBoat(2499) == 3

def test_importData():
    data = importData("test_container.xlsx")
    assert len(data) == 99
    assert data.iloc[0,0] == "CN0001"
    assert data.iloc[0,1] == 1516
    assert data.iloc[0,2] == "China"
    assert data.iloc[0,3] == datetime.datetime(2024, 3, 17, 9, 0)
    assert data.iloc[0,4] == "INBOUND"
    assert data.iloc[0,5] == 1
    assert data.iloc[98,0] == "US0003"
    assert data.iloc[98,1] == 1157
    assert data.iloc[98,2] == "America"
    assert data.iloc[98,3] == datetime.datetime(2024, 4, 3, 14, 0)
    assert data.iloc[98,4] == "INBOUND"
    assert data.iloc[98,5] == 1

def test_str_to_date():
    assert str_to_date("2024-03-17 09:00") == datetime.date(2024, 3, 17)
    assert str_to_date("2024-04-03 02:00") == datetime.date(2024, 4, 3)

def test_ifrepeat():
    data = importData("test_container.xlsx")
    ContainerBoat.objects.all().delete()
    assert ifrepeat(data.iloc[0,:]) == False
    ContainerBoat.objects.create(ContainerBoatID="CN0001", Tonnage=1516, Country="China")
    assert ifrepeat(data.iloc[0,:]) == True
    ContainerBoat.objects.all().delete()

def test_dataIntoDatabase_ContainerBoat():
    data = importData("test_container.xlsx")
    dataIntoDatabase_ContainerBoat(data)
    assert len(ContainerBoat.objects.all()) == 98
    assert ContainerBoat.objects.get(ContainerBoatID="CN0001").Tonnage == 1516
    assert ContainerBoat.objects.get(ContainerBoatID="CN0001").Country == "China"
    assert ContainerBoat.objects.get(ContainerBoatID="US0003").Tonnage == 1157
    assert ContainerBoat.objects.get(ContainerBoatID="US0003").Country == "America"

def test_dataIntoDatabase_TugBoat():
    TugBoat.objects.all().delete()
    data = pd.DataFrame({
        'TugBoatId': ["TB001", "TB002", "TB003"],
        'CurrentStatus': ["Available", "Maintenance", "Available"],
        'CaptainId': [1, 2, 3],
        'StartWorkingTime': ["09:00", "10:00", "09:00"],
        'EndWorkingTime': ["18:00", "17:00", "18:00"]
    })
    Captain.objects.create(CaptainId=1, Account=None)
    Captain.objects.create(CaptainId=2, Account=None)
    Captain.objects.create(CaptainId=3, Account=None)
    dataIntoDatabase_TugBoat(data)
    assert len(TugBoat.objects.all()) == 3
    assert TugBoat.objects.get(TugBoatId="TB001").CurrentStatus == "Available"
    assert TugBoat.objects.get(TugBoatId="TB001").CaptainId.CaptainId == '1'
    assert TugBoat.objects.get(TugBoatId="TB002").CurrentStatus == "Maintenance"
    assert TugBoat.objects.get(TugBoatId="TB002").CaptainId.CaptainId == '2'
    assert TugBoat.objects.get(TugBoatId="TB003").CurrentStatus == "Available"
    assert TugBoat.objects.get(TugBoatId="TB003").CaptainId.CaptainId == '3'
    Captain.delete(Captain.objects.get(CaptainId=1))
    Captain.delete(Captain.objects.get(CaptainId=2))
    Captain.delete(Captain.objects.get(CaptainId=3))
    TugBoat.objects.all().delete()

def test_IfTaskRepeat():
    Berth.objects.create(BerthId=11)
    Task.objects.create(ContainerBoatID=ContainerBoat.objects.get(ContainerBoatID="CN0001"), BerthId=Berth.objects.get(BerthId=11).BerthId, startTime=datetime.datetime(2024, 3, 17, 9, 0), Action="INBOUND")
    assert IfTaskRepeat(["CN0001", 1516, "China", "2024-03-17 09:00", "INBOUND", 11]) == True
    assert IfTaskRepeat(["CN0002", 1516, "China", "2024-03-17 09:00", "INBOUND", 1]) == False
    Task.objects.all().delete()
    Berth.delete(Berth.objects.get(BerthId=11))
    ContainerBoat.objects.all().delete()


def test_createTask():
    data = importData("test_container.xlsx")
    dataIntoDatabase_ContainerBoat(data)
    data = pd.read_excel("test_tug.xlsx", header=None)
    data=data.iloc[1:,:]
    df=pd.DataFrame(data)
    df.columns=['TugBoatId','CurrentStatus','CaptainId','StartWorkingTime','EndWorkingTime']
    dataIntoDatabase_TugBoat(df)
    data = importData("test_container.xlsx")
    createTask(data)
    assert len(Task.objects.all()) == 99
    ContainerBoat.objects.all().delete()
    TugBoat.objects.all().delete()
    Task.objects.all().delete()
    ScheduleEntry.objects.all().delete()

if __name__ == '__main__':
    pytest.main(["-v", "--tb=line", "test_importData.py"])
