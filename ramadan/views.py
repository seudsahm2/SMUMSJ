# ramadan/views.py
from django.views.generic import DetailView
from hijri_converter import Hijri


class RamadanTracker(DetailView):
    template_name = 'special/ramadan_tracker.html'

    def get_object(self):
        hijri_date = Hijri.today()
        if hijri_date.month == 9:
            return {
                'current_day': hijri_date.day,
                'checklist': RamadanChecklist.objects.get(day=hijri_date.day)
            }
        return {'current_day': None}

    def post(self, request):
        day = request.POST.get('day')
        progress, _ = UserProgress.objects.update_or_create(
            user=request.user,
            day_id=day,
            defaults={'completed': True}
        )
        return redirect('ramadan-tracker')
