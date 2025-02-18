from django.contrib import admin
from .models import FinancialRecord


@admin.register(FinancialRecord)
class FinancialRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'record_type', 'amount', 'added_by')
    list_filter = ('record_type', 'date')
    search_fields = ('description', 'added_by__email')
