from django.urls import path
from .views import PrayerWallView, CreatePrayerRequestView, PrayerTimesView

app_name = 'prayer'
urlpatterns = [
    path('wall/', PrayerWallView.as_view(), name='prayer-wall'),
    path('create/', CreatePrayerRequestView.as_view(), name='create-request'),
    path('times/', PrayerTimesView.as_view(), name='times'),
]
