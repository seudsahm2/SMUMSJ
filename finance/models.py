from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FinancialRecord(models.Model):
    RECORD_TYPES = (
        ('DONATION', 'Donation'),
        ('SPONSOR', 'Sponsorship'),
        ('EXPENSE', 'Expense'),
    )
    
    record_type = models.CharField(max_length=10, choices=RECORD_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Financial Record"

    def __str__(self):
        return f"{self.get_record_type_display()} - {self.amount}"