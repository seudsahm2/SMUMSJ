from django.urls import path
from .views import DonationCreateView
from .views import CampaignListView
app_name = 'charity'

urlpatterns = [
    path('donate/', DonationCreateView.as_view(), name='donate'),
    path('campaigns/', CampaignListView.as_view(), name='campaigns'),
]
