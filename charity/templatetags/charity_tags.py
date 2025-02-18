
# charity/templatetags/charity_tags.py
from django import template
from charity.models import Donation
register = template.Library()

@register.simple_tag
def campaign_progress(campaign_name):
    total = Donation.objects.filter(campaign=campaign_name).aggregate(
        Sum('amount')
    )['amount__sum'] or 0
    target = 200 * 50  # Example: 200 families × 50 USD
    return min(int((total / target) * 100), 100)