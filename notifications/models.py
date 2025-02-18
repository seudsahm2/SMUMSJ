# notifications/models.py (new app)
from django.db import models
from accounts.models import CustomUser


class Notification(models.Model):
    TYPES = (
        ('FRIDAY', 'Friday Reminder'),
        ('EVENT', 'Event Alert'),
        ('DONATION', 'Donation Update'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    notification_type = models.CharField(max_length=10, choices=TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
