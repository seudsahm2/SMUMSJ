# resources/views.py
from django.views.generic import ListView, DetailView
from .models import IslamicResource


class ResourceListView(ListView):
    model = IslamicResource
    template_name = 'resources/list.html'
    paginate_by = 10


class ResourceDownloadView(DetailView):
    model = IslamicResource

    def get(self, request, *args, **kwargs):
        resource = self.get_object()
        resource.downloads += 1
        resource.save()
        return redirect(resource.file.url)
