import django_tables2 as tables
from .models import FinancialRecord


class FinancialRecordTable(tables.Table):
    actions = tables.TemplateColumn(
        template_name='finance/actions_column.html',
        orderable=False,
        attrs={"td": {"class": "text-center"}}
    )

    class Meta:
        model = FinancialRecord
        fields = ('date', 'record_type', 'amount',
                  'related_user', 'verified_by')
        attrs = {
            "class": "table table-hover islamic-table",
            "thead": {"class": "thead-light"}
        }
