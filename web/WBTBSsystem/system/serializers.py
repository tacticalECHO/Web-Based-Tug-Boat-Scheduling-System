from rest_framework import serializers
from .models import Captain, TugBoat, Task, Scheduler, ContainerBoat, Berth, ScheduleEntry

class TugBoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TugBoat
        fields = ['TugBoatId', 'CurrentStatus']

class CaptainSerializer(serializers.ModelSerializer):
    tugboat = TugBoatSerializer(read_only=True)
    class Meta:
        model = Captain
        fields = ['name', 'CaptainId', 'tugboat']

class SchedulerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduler
        fields = ['name', 'SchedulerId']

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff']

class ContainerBoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerBoat
        fields = ['ContainerBoatID', 'Tonnage', 'Country', 'arrivalTime', 'departureTime']
        
class BerthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Berth
        fields = ['BerthId', 'ContainerBoat']

class TaskSerializer(serializers.ModelSerializer):
    ContainerBoatID = ContainerBoatSerializer()
    class Meta:
        model = Task
        fields = ['TaskId', 'RequiredTugBoat', 'startTime', 'endTime', 'ContainerBoatID', 'Action', 'BerthId', 'State']

class TugBoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TugBoat
        fields = ['CurrentStatus', 'TugBoatId', 'CaptainId ', 'StartWorkingTime', 'EndWorkingTime']

class ScheduleEntrySerializer(serializers.ModelSerializer):
    TaskId = TaskSerializer()
    listOfTugBoats = TugBoatSerializer()
    class Meta:
        model = ScheduleEntry
        fields = ['ScheduleEntryId', 'listOfTugBoats', 'TaskId', 'State']
