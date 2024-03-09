# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Captain(models.Model): # Captain model
    Account = models.OneToOneField(User, on_delete=models.CASCADE, related_name='captain', null=True, blank=True)
    name = models.CharField(max_length=200)
    CaptainId = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.CaptainId
    def save(self, *args, **kwargs):
        if not self.Account:
            user = User.objects.filter(username=self.CaptainId).first()
            if user:
                self.Account = user 
        super(Captain, self).save(*args, **kwargs)

class Scheduler(models.Model): # Scheduler model
    Account = models.OneToOneField(User, on_delete=models.CASCADE, related_name='scheduler', null=True, blank=True)
    name = models.CharField(max_length=200)
    SchedulerId = models.CharField(max_length=200, unique=True)
    def save(self, *args, **kwargs):
        if not self.Account:  
            user = User.objects.filter(username=self.SchedulerId).first()
            if user:
                self.Account = user 
        super(Scheduler, self).save(*args, **kwargs)

class TugBoat(models.Model): #TugBoat model
    CurrentStatus = models.CharField(max_length=20,choices=(('Free','Free'),('Busy','Busy'),('Maintenance','Maintenance')),default='Free')
    TugBoatId = models.CharField(max_length=200, unique=True) 
    CaptainId = models.OneToOneField(Captain, on_delete=models.CASCADE, related_name='tugboat', null=True)
    StartWorkingTime = models.TimeField(default='T00:00:00Z')
    EndWorkingTime = models.TimeField(default='T08:00:00Z')
    def __str__(self):
        return self.TugBoatId
    
class ContainerBoat(models.Model): # ContainerBoat model
    ContainerBoatID = models.CharField(max_length=200)
    Tonnage = models.IntegerField(default=0)
    Country = models.CharField(max_length=200)
    def __str__(self):
        return self.ContainerBoatID

class Task(models.Model): # Task model
    TaskId = models.AutoField(primary_key=True)
    RequiredTugBoat = models.IntegerField(default=0)
    startTime = models.DateTimeField()
    ContainerBoatID = models.ForeignKey(ContainerBoat, on_delete=models.CASCADE)
    Action = models.CharField(max_length=10,choices=(('INBOUND','INBOUND'),('OUTBOUND','OUTBOUND')),default='INBOUND')
    BerthId = models.IntegerField(default=0)
    State = models.CharField(max_length=100,choices=(('Scheduled','Scheduled'),('Unscheduled','Unscheduled')),default='Unscheduled')
    TaskManual = models.IntegerField(default=0)
    def __int__(self):
        return self.TaskId
    def save(self, *args, **kwargs):
        if not self.TaskId:  
            task = Task.objects.filter(TaskId=self.TaskId).first()
            if task:
                self.TaskId = task 
        super(Task, self).save(*args, **kwargs)
    
class ScheduleEntry(models.Model): # ScheduleEntry model
    ScheduleEntryId= models.AutoField(primary_key=True)
    listOfTugBoats = models.ManyToManyField(TugBoat)
    TaskId = models.ForeignKey(Task, on_delete=models.CASCADE)
    Status = models.CharField(max_length=10,choices=(('Scheduled','Scheduled'),('Completed','Completed'),('Confirmed','Confirmed')),default='Scheduled')
    PublishTime = models.DateTimeField()
    StartTime = models.DateTimeField(null=True,blank=True)
    EndTime = models.DateTimeField(null=True,blank=True)
    def __int__(self):
        return self.ScheduleEntryId
    # def save(self, *args, **kwargs):
    #     if not self.ScheduleEntryId:  
    #         scheduleEntry = ScheduleEntry.objects.filter(ScheduleEntryId=self.ScheduleEntryId).first()
    #         if scheduleEntry:
    #             self.ScheduleEntryId = scheduleEntry 
    #     super(ScheduleEntry, self).save(*args, **kwargs)

class Berth(models.Model): # Berth model
    BerthId= models.IntegerField(primary_key=True)
    ContainerBoat= models.OneToOneField(ContainerBoat, on_delete=models.CASCADE,null=True,related_name='berth',blank=True)
    def __str__(self):
       return str(self.BerthId)
