# backend/api/urls.py

from django.urls import path, include
from rest_framework import routers
from .views import AirQualitySensorViewSet, AirQualityReadingViewSet

router = routers.DefaultRouter()
router.register(r'sensors', AirQualitySensorViewSet)
router.register(r'readings', AirQualityReadingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns += [
    path('predict/', AirQualityPredictionView.as_view(), name='air-quality-prediction'),
]