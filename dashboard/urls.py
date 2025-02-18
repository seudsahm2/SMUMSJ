from django.urls import path
from .views import MemberDashboard, AmirDashboard

app_name = 'dashboard'

urlpatterns = [
    path('', MemberDashboard.as_view(), name='member-dashboard'),
    path('amir/', AmirDashboard.as_view(), name='amir-dashboard'),
]
