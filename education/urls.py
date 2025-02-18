from django.urls import path
from .views import TutorRequestView, ResourceListView

app_name = 'education'
urlpatterns = [
    path('tutor/', TutorRequestView.as_view(), name='tutor-request'),
    path('materials/', ResourceListView.as_view(), name='education-resources'),
]
