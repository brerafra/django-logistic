from rest_framework import fields, serializers

from .models import Vehicle,Event

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Vehicle
        fields='__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model= Event
        fields='__all__'