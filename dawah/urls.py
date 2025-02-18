from django.urls import path
from .views import DailyHadithView, AskImamView

app_name = 'dawah'
urlpatterns = [
    path('daily-hadith/', DailyHadithView.as_view(), name='daily-hadith'),
    path('ask-imam/', AskImamView.as_view(), name='ask-imam'),
]
