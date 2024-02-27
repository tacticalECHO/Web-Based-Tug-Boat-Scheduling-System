from rest_framework import serializers
from .models import Captain, TugBoat, Scheduler

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