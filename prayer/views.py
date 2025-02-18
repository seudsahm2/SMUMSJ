from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import PrayerRequest, PrayerTime
from .forms import PrayerRequestForm, PrayerTimeFilterForm


class PrayerWallView(ListView):
    model = PrayerRequest
    template_name = 'prayer/wall.html'
    context_object_name = 'requests'
    paginate_by = 15

    def get_queryset(self):
        return PrayerRequest.objects.filter(is_public=True).order_by('-created_at')


class CreatePrayerRequestView(LoginRequiredMixin, CreateView):
    model = PrayerRequest
    form_class = PrayerRequestForm
    template_name = 'prayer/create_request.html'
    success_url = reverse_lazy('prayer-wall')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PrayerTimesView(ListView):
    model = PrayerTime
    template_name = 'prayer/times.html'
    context_object_name = 'prayer_times'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = PrayerTimeFilterForm()
        return context
