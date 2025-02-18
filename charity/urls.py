from django.urls import path
from .views import DonationCreateView

app_name = 'charity'

urlpatterns = [
    path('<str:campaign>/', DonationCreateView.as_view(), name='donate'),
    path('campaigns/', DonationCreateView.as_view(), name='campaigns'),
]
