from django.urls import path
from .views import FinanceReportView, AddFinancialRecordView

app_name = 'finance'
urlpatterns = [
    path('report/', FinanceReportView.as_view(), name='finance-report'),
    path('add/', AddFinancialRecordView.as_view(), name='add-record'),
]
