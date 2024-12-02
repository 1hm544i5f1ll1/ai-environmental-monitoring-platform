# backend/api/serializers.py

from rest_framework import serializers
from .models import AirQualitySensor, AirQualityReading

class AirQualitySensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirQualitySensor
        fields = ['id', 'name', 'location', 'created_at']

class AirQualityReadingSerializer(serializers.ModelSerializer):
    sensor = AirQualitySensorSerializer(read_only=True)
    sensor_id = serializers.PrimaryKeyRelatedField(
        queryset=AirQualitySensor.objects.all(), source='sensor', write_only=True
    )

    class Meta:
        model = AirQualityReading
        fields = ['id', 'sensor', 'sensor_id', 'pm2_5', 'pm10', 'no2', 'so2', 'o3', 'timestamp']
        read_only_fields = ['id', 'sensor', 'timestamp']
