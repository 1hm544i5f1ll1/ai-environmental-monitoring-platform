from django.db import models

# Create your models here.
# backend/api/models.py

from django.db import models

class AirQualitySensor(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class AirQualityReading(models.Model):
    sensor = models.ForeignKey(AirQualitySensor, on_delete=models.CASCADE, related_name='readings')
    pm2_5 = models.FloatField()
    pm10 = models.FloatField()
    no2 = models.FloatField()
    so2 = models.FloatField()
    o3 = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sensor.name} - {self.timestamp}"
