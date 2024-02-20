from django.db import models

# Create your models here.
from django.db import models

class Members(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)
class Captain(models.Model):
    name = models.CharField(max_length=200)
    CaptainId = models.IntegerField(default=0)

class TugBoat(models.Model):
    CurrentStatus = models.CharField(max_length=20,choices=(('Free','Free'),('Busy','Busy'),('Maintenance','Maintenance')),default='Free')
    TugBoatId = models.IntegerField(default=0)
    CaptainId = models.ForeignKey(Captain, on_delete=models.CASCADE)
    StartWorkingTime = models.TimeField(default='T00:00:00Z')
    EndWorkingTime = models.TimeField(default='T08:00:00Z')
    
class ContainerBoat(models.Model):
    ContainerBoatID = models.IntegerField(default=0)
    Tonnage = models.IntegerField(default=0)
    Country = models.CharField(max_length=200)
    arrivalTime = models.DateTimeField()
    departureTime = models.DateTimeField()

class Task(models.Model):
    TaskId = models.AutoField(primary_key=True)
    ReqauriedTugBoat = models.IntegerField(default=0)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    ContainerBoatID = models.ForeignKey(ContainerBoat, on_delete=models.CASCADE)
    Action= models.CharField(max_length=10,choices=(('Arrival','Arrival'),('Departure','Departure')),default='Arrival')
    BerthId = models.IntegerField(default=0)
    State = models.CharField(max_length=100,choices=(('Scheduled','Scheduled'),('Unscheduled','Unscheduled')),default='Unscheduled')

class ScheduleEntry(models.Model):
    ScheduleEntryId= models.AutoField(primary_key=True)
    listOfTugBoats = models.ManyToManyField(TugBoat)
    TaskId = models.ForeignKey(Task, on_delete=models.CASCADE)
    State = models.CharField(max_length=10,choices=(('Scheduled','Scheduled'),('Completed','Completed')),default='Scheduled')

class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Role = models.CharField(max_length=200)
