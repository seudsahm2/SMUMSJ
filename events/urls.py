from django.urls import path
from .views import EventListView, EventDetailView, EventRegistrationView

app_name = 'events'

urlpatterns = [
    path('', EventListView.as_view(), name='event-list'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path("event/<int:pk>/register/",
         EventRegistrationView.as_view(), name="event_register"),
]
