from django.contrib import admin

# Register your models here.
# backend/api/admin.py

from django.contrib import admin
from .models import AirQualitySensor, AirQualityReading

@admin.register(AirQualitySensor)
class AirQualitySensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'created_at')
    search_fields = ('name', 'location')

@admin.register(AirQualityReading)
class AirQualityReadingAdmin(admin.ModelAdmin):
    list_display = ('id', 'sensor', 'pm2_5', 'pm10', 'no2', 'so2', 'o3', 'timestamp')
    list_filter = ('sensor', 'timestamp')
    search_fields = ('sensor__name',)
