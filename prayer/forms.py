from django import forms
from .models import PrayerRequest


class PrayerRequestForm(forms.ModelForm):
    class Meta:
        model = PrayerRequest
        fields = ['request', 'is_public']
        widgets = {
            'request': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write your prayer request here...',
                'class': 'islamic-textarea'
            }),
            'is_public': forms.CheckboxInput(attrs={
                'class': 'islamic-checkbox'
            })
        }


class PrayerTimeFilterForm(forms.Form):
    month = forms.ChoiceField(choices=[(i, i) for i in range(1, 13)])
    year = forms.ChoiceField(choices=[(i, i) for i in range(2020, 2030)])
