# filepath: /D:/projects/django_project/SMUMSJ/jamaa_site/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import SignupView
from accounts.forms import CustomSignupForm

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    path('accounts/signup/', SignupView.as_view(form_class=CustomSignupForm),
         name='account_signup'),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),

    # Apps
    path('', include('dashboard.urls')),
    path('charity/', include('charity.urls', namespace='charity')),
    path('events/', include('events.urls', namespace='events')),
    path('dawah/', include('dawah.urls', namespace='dawah')),
    path('education/', include('education.urls', namespace='education')),
    path('finance/', include('finance.urls', namespace='finance')),
    path('resources/', include('resources.urls', namespace='resources')),
    path('ramadan/', include('ramadan.urls', namespace='ramadan')),
    path('prayer/', include('prayer.urls', namespace='prayer')),

    # Profile
    path('accounts/profile/', include('profiles.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
