# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Captain(models.Model): # Captain model
    Account = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    CaptainId = models.CharField(max_length=200, unique=True) 


class TugBoat(models.Model): #@ TugBoat model
    CurrentStatus = models.CharField(max_length=20,choices=(('Free','Free'),('Busy','Busy'),('Maintenance','Maintenance')),default='Free')
    TugBoatId = models.CharField(max_length=200, unique=True) 
    CaptainId = models.OneToOneField(Captain, on_delete=models.CASCADE, related_name='tugboat', null=True)
    StartWorkingTime = models.TimeField(default='T00:00:00Z')
    EndWorkingTime = models.TimeField(default='T08:00:00Z')
    
class ContainerBoat(models.Model): # ContainerBoat model
    ContainerBoatID = models.CharField(max_length=200)
    Tonnage = models.IntegerField(default=0)
    Country = models.CharField(max_length=200)
    arrivalTime = models.DateTimeField()
    departureTime = models.DateTimeField()

class Task(models.Model): # Task model
    TaskId = models.AutoField(primary_key=True)
    ReqauriedTugBoat = models.IntegerField(default=0)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    ContainerBoatID = models.ForeignKey(ContainerBoat, on_delete=models.CASCADE)
    Action= models.CharField(max_length=10,choices=(('Arrival','Arrival'),('Departure','Departure')),default='Arrival')
    BerthId = models.IntegerField(default=0)
    State = models.CharField(max_length=100,choices=(('Scheduled','Scheduled'),('Unscheduled','Unscheduled')),default='Unscheduled')

class ScheduleEntry(models.Model): # ScheduleEntry model
    ScheduleEntryId= models.AutoField(primary_key=True)
    listOfTugBoats = models.ManyToManyField(TugBoat)
    TaskId = models.ForeignKey(Task, on_delete=models.CASCADE)
    State = models.CharField(max_length=10,choices=(('Scheduled','Scheduled'),('Completed','Completed')),default='Scheduled')

class Scheduler(models.Model): # Scheduler model
    Account = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    SchedulerId = models.CharField(max_length=200, unique=True)

