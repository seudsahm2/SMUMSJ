# filepath: /D:/projects/django_project/SMUMSJ/resources/urls.py
from django.urls import path
from .views import ResourceListView, ResourceDownloadView

app_name = 'resources'

urlpatterns = [
    path('', ResourceListView.as_view(), name='resource-list'),
    path('<int:pk>/download/', ResourceDownloadView.as_view(),
         name='resource-download'),
]
