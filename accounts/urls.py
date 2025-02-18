from django.urls import path
from .views import ProfileView

app_name = 'accounts'

urlpatterns = [
    path('', ProfileView.as_view(), name='member-profile'),
]
