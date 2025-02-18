from django.views.generic import ListView, DetailView
from .models import Event, EventRegistration
from django.utils import timezone
from django.shortcuts import redirect

class EventListView(ListView):
    model = Event
    template_name = 'departments/events/list.html'
    ordering = ['-date']

    def get_queryset(self):
        return Event.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = self.get_queryset()
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = 'departments/events/detail.html'

    def post(self, request, *args, **kwargs):
        event = self.get_object()
        EventRegistration.objects.get_or_create(user=request.user, event=event)
        return redirect('event-detail', pk=event.pk)