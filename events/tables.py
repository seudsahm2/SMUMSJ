# events/tables.py
import django_tables2 as tables
from .models import Event


class EventTable(tables.Table):
    actions = tables.TemplateColumn(
        template_name='departments/events/actions_column.html',
        orderable=False
    )

    class Meta:
        model = Event
        fields = ('title', 'event_type', 'date', 'location')
