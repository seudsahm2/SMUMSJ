from django.contrib import admin
from .models import PrayerRequest, PrayerTime


@admin.register(PrayerRequest)
class PrayerRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'is_public', 'is_answered')
    list_filter = ('is_public', 'is_answered', 'created_at')
    search_fields = ('request', 'user__email')
    date_hierarchy = 'created_at'


@admin.register(PrayerTime)
class PrayerTimeAdmin(admin.ModelAdmin):
    list_display = ('date', 'hijri_date', 'fajr',
                    'dhuhr', 'asr', 'maghrib', 'isha')
    list_filter = ('date',)
    search_fields = ('hijri_date',)
    ordering = ('-date',)
