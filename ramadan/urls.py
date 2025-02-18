from django.urls import path
from .views import RamadanTracker

app_name = 'ramadan'
urlpatterns = [
    path('', RamadanTracker.as_view(), name='ramadan-tracker'),
]
