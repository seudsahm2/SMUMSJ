# charity/templatetags/charity_tags.py
from django import template
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.db.models import Value, DecimalField
from charity.models import Donation
from decimal import Decimal
register = template.Library()

@register.simple_tag
def campaign_progress(campaign):
    if not campaign:
        return 0.0
    
    total = Donation.objects.filter(campaign=campaign).aggregate(
        total_amount=Coalesce(Sum('amount'), Value(0.0, output_field=DecimalField(max_digits=10, decimal_places=2)))
    )['total_amount']
    
    goal = campaign.goal_amount
    if goal > 0:
        progress = (total / goal) * Decimal('100.0')  # Use float multiplier
        return min(float(progress), 100.0)
    return 0.0