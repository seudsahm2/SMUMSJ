from django.views.generic import ListView, DetailView, View
from .models import Event, EventRegistration
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from .forms import EventRegistrationForm
from django.views import View
from django.utils.decorators import method_decorator
from .forms import EventRegistrationForm
from django.utils.timezone import now


class EventListView(ListView):
    model = Event
    template_name = 'departments/events/list.html'
    context_object_name = 'events'

    def get_queryset(self):
        # Order events by date (latest first)
        return Event.objects.order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_time = now()

        # Separate events into upcoming and previous
        context['upcoming_events'] = Event.objects.filter(date__gte=current_time).order_by('date')
        context['previous_events'] = Event.objects.filter(date__lt=current_time).order_by('-date')

        return context


class EventDetailView(DetailView):
    model = Event
    template_name = "departments/events/detail.html"
    context_object_name = "event"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = self.get_object()
        user = self.request.user

        # Check if the user is already registered
        context["is_registered"] = (
            EventRegistration.objects.filter(event=event, user=user).exists()
            if user.is_authenticated
            else False
        )
        context["form"] = EventRegistrationForm()
        return context


@method_decorator(login_required, name='dispatch')
class EventRegistrationView(View):
    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        user = request.user

        # Check if the user is already registered
        if EventRegistration.objects.filter(event=event, user=user).exists():
            return JsonResponse({"message": "You are already registered!"}, status=400)

        # Register the user
        EventRegistration.objects.create(event=event, user=user)

        # Return updated attendee count
        return JsonResponse({"attendee_count": event.registrations.count()})
