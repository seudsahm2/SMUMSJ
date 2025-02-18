from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class PrayerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_public = models.BooleanField(default=True)
    is_answered = models.BooleanField(default=False)
    answered_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Prayer Request"
        verbose_name_plural = "Prayer Requests"

    def __str__(self):
        return f"Prayer request by {self.user} on {self.created_at.date()}"


class PrayerTime(models.Model):
    date = models.DateField(unique=True)
    hijri_date = models.CharField(max_length=50)
    fajr = models.TimeField()
    dhuhr = models.TimeField()
    asr = models.TimeField()
    maghrib = models.TimeField()
    isha = models.TimeField()

    class Meta:
        ordering = ['-date']
        verbose_name = "Prayer Time"
        verbose_name_plural = "Prayer Times"

    def __str__(self):
        return f"Prayer times for {self.date}"
