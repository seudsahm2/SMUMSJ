# dashboard/admin.py
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'date', 'admin_actions')

    def admin_actions(self, obj):
        return format_html(
            '<a href="{}">Edit</a> | <a href="{}">Delete</a>',
            reverse('admin:events_event_change', args=[obj.id]),
            reverse('admin:events_event_delete', args=[obj.id])
        )
    admin_actions.short_description = 'Actions'
