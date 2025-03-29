import logging
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from events.models import Event
from django.utils import timezone
from charity.models import Donation,Campaign
from datetime import datetime
from django.db.models import F, ExpressionWrapper, FloatField, Sum, Exists, OuterRef,DecimalField,Value
from django.db.models.functions import Coalesce


# Set up logging
logger = logging.getLogger(__name__)

class MemberDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/member.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        context['current_date'] = timezone.now()
        context['upcoming_events'] = Event.objects.filter(
            date__gte=timezone.now()
        )[:3]
        context['previous_events'] = Event.objects.filter(
            date__lt=timezone.now()
        )
        context['recent_donations'] = Donation.objects.filter(
            donor=self.request.user
        ).order_by('-donated_at')[:5]

        
        context['active_campaigns'] = Campaign.objects.annotate(
            total_donations=Coalesce(
                Sum('donation__amount', output_field=DecimalField(max_digits=10, decimal_places=2)),
                Value(0.0, output_field=DecimalField(max_digits=10, decimal_places=2))
            ),
            progress=ExpressionWrapper(
                (F('total_donations') / F('goal_amount')) * 100,
                output_field=DecimalField(max_digits=5, decimal_places=1)
            ),
            has_donated=Exists(
                Donation.objects.filter(campaign=OuterRef('pk'), donor=user)
                if user.is_authenticated else Value(False)
            )
        ).order_by('progress')[:2]
        

        # Debugging Logs
        logger.debug(f"Current date: {context['current_date']}")
        logger.debug(f"Upcoming events: {context['upcoming_events']}")
        logger.debug(f"Recent donations: {context['recent_donations']}")
        logger.debug(f"Active campaigns: {context['active_campaigns']}")

        print(f"Current date: {context['current_date']}")
        print(f"Upcoming events: {context['upcoming_events']}")
        print(f"Recent donations: {context['recent_donations']}")
        print(f"Active campaigns: {context['active_campaigns']}")

        return context

class AmirDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/amir.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_members'] = CustomUser.objects.filter(
            role__in=['MEMBER', 'AMIR']
        ).count()
        context['active_events'] = Event.objects.filter(
            date__gte=timezone.now()
        )
        context['users'] = CustomUser.objects.filter(
            role__in=['MEMBER', 'AMIR']
        )

        # Debugging code
        logger.debug(f"Total members: {context['total_members']}")
        logger.debug(f"Active events: {context['active_events']}")
        logger.debug(f"Users: {context['users']}")

        print(f"Total members: {context['total_members']}")
        print(f"Active events: {context['active_events']}")
        print(f"Users: {context['users']}")

        return context
