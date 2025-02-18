from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Hadith, ScholarLecture, Question
from .forms import AskImamForm


class DailyHadithView(ListView):
    template_name = 'dawah/daily_hadith.html'
    context_object_name = 'hadiths'

    def get_queryset(self):
        return Hadith.objects.filter(date__lte=timezone.now()).order_by('-date')[:7]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today_hadith'] = Hadith.objects.filter(
            date=timezone.now().date()).first()
        context['upcoming_lectures'] = ScholarLecture.objects.filter(
            date__gte=timezone.now())[:3]
        return context


class AskImamView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = AskImamForm
    template_name = 'dawah/ask_imam.html'
    success_url = reverse_lazy('ask-imam')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answered_questions'] = Question.objects.filter(
            is_public=True,
            answer__isnull=False
        ).order_by('-asked_on')[:10]
        return context
