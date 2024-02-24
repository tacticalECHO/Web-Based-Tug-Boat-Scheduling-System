from rest_framework import serializers
from .models import Captain, TugBoat

class TugBoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TugBoat
        fields = ['TugBoatId', 'CurrentStatus']

class CaptainSerializer(serializers.ModelSerializer):
    tugboat = TugBoatSerializer(read_only=True)
    class Meta:
        model = Captain
        fields = ['name', 'CaptainId', 'tugboat']