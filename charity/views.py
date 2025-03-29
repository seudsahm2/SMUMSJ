# charity/views.py
from django.views.generic import ListView
from .models import Campaign, Donation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Exists, OuterRef, Sum

# charity/views.py
from .forms import DonationForm

class DonationCreateView(LoginRequiredMixin, CreateView):
    model = Donation
    form_class = DonationForm  # Use custom form instead of fields
    template_name = 'departments/charity/donate.html'
    success_url = reverse_lazy('charity:campaigns')

    def get_initial(self):
        initial = super().get_initial()
        campaign_id = self.request.GET.get('campaign')
        if campaign_id:
            try:
                campaign = Campaign.objects.get(id=campaign_id)
                # Check if campaign is still active
                total_donations = Donation.objects.filter(campaign=campaign).aggregate(
                    total=Sum('amount')
                )['total'] or 0
                if total_donations < campaign.goal_amount:
                    initial['campaign'] = campaign_id
                else:
                    messages.error(self.request, "This campaign has already ended")
            except Campaign.DoesNotExist:
                pass
        return initial

    def form_valid(self, form):
        form.instance.donor = self.request.user
        campaign = form.cleaned_data['campaign']
        # Final validation check
        total_donations = Donation.objects.filter(campaign=campaign).aggregate(
            total=Sum('amount')
        )['total'] or 0
        
        if total_donations >= campaign.goal_amount:
            form.add_error('campaign', "This campaign has already ended")
            return self.form_invalid(form)
            
        messages.success(self.request, "Thank you for your donation!")
        return super().form_valid(form)

class CampaignListView(ListView):
    model = Campaign
    template_name = 'departments/charity/campaigns.html'
    context_object_name = 'campaigns'

    def get_queryset(self):
        # Annotate each campaign with a flag indicating if the user has donated and total donations
        user = self.request.user
        queryset = Campaign.objects.annotate(
            total_donations=Sum('donation__amount')  # Sum of all donations for each campaign
        )
        if user.is_authenticated:
            queryset = queryset.annotate(
                has_donated=Exists(
                    Donation.objects.filter(campaign=OuterRef('pk'), donor=user)
                )
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculate total raised across all campaigns
        total_raised = Donation.objects.aggregate(Sum('amount'))['amount__sum'] or 0
        # Calculate total number of unique donors
        total_donors = Donation.objects.values('donor').distinct().count()
        context['total_raised'] = total_raised
        context['total_donors'] = total_donors
        return context