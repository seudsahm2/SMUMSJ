from django import forms
from .models import Donation, Campaign
from django.db.models import Sum, F, Value,DecimalField
from django.db.models.functions import Coalesce
from django.db.models.expressions import ExpressionWrapper

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['amount', 'campaign']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campaign'].queryset = Campaign.objects.annotate(
            total_donations=Coalesce(Sum('donation__amount'), 
                Value(0.0, output_field=DecimalField(max_digits=10, decimal_places=2))
            ),
            remaining=ExpressionWrapper(
                F('goal_amount') - F('total_donations'),
                output_field=DecimalField(max_digits=10, decimal_places=2)
            )
        ).filter(remaining__gt=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show active campaigns (progress < 100%)
        self.fields['campaign'].queryset = Campaign.objects.annotate(
            total_donations=Coalesce(Sum('donation__amount'), Value(0,output_field=DecimalField(max_digits=10, decimal_places=2)))
        ).filter(
            total_donations__lt=F('goal_amount')
        )

    def clean_campaign(self):
        campaign = self.cleaned_data['campaign']
        total_donations = Donation.objects.filter(campaign=campaign).aggregate(
            total=Sum('amount',output_field=DecimalField(max_digits=10, decimal_places=2))
        )['total'] or 0
        
        if total_donations >= campaign.goal_amount:
            raise forms.ValidationError("This campaign has already reached its goal.")
        return campaign