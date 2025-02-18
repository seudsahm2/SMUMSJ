from django import forms
from .models import Question


class AskImamForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question']
        widgets = {
            'question': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Type your Islamic question here...'
            }),
        }
