# education/views.py
from django.views.generic import CreateView, ListView
from .models import TutorRequest, EducationalResource


class TutorRequestView(CreateView):
    model = TutorRequest
    fields = ['subject', 'description']
    template_name = 'departments/education/tutor_request.html'

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)


class ResourceListView(ListView):
    model = EducationalResource
    template_name = 'departments/education/resources.html'
    paginate_by = 10
    filterset_fields = ['subject']
