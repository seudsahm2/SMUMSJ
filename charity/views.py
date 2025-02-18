# charity/views.py
from django import template
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Donation


class DonationCreateView(LoginRequiredMixin, CreateView):
    model = Donation
    fields = ['amount', 'campaign']
    template_name = 'departments/charity/donate.html'

    def form_valid(self, form):
        form.instance.donor = self.request.user
        return super().form_valid(form)
