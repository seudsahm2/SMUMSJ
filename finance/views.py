from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import FinancialRecord
from .forms import FinancialRecordForm

class FinanceReportView(LoginRequiredMixin, ListView):
    model = FinancialRecord
    template_name = 'finance/report.html'
    context_object_name = 'records'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_income'] = FinancialRecord.objects.filter(
            record_type__in=['DONATION', 'SPONSOR']
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        context['total_expenses'] = FinancialRecord.objects.filter(
            record_type='EXPENSE'
        ).aggregate(Sum('amount'))['amount__sum'] or 0
        
        return context

class AddFinancialRecordView(LoginRequiredMixin, CreateView):
    model = FinancialRecord
    form_class = FinancialRecordForm
    template_name = 'finance/add_record.html'
    success_url = reverse_lazy('finance-report')

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)