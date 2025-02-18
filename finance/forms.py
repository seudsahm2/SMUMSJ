from django import forms
from .models import FinancialRecord


class FinancialRecordForm(forms.ModelForm):
    class Meta:
        model = FinancialRecord
        fields = ['record_type', 'amount', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
