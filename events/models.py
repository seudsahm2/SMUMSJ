from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    event_type = models.CharField(max_length=50)
    images = models.ImageField(upload_to="event_images/")

    def __str__(self):
        return self.title

    def attendee_count(self):
        return self.registrations.count()  # Related name used in EventRegistration


class EventRegistration(models.Model):
    event = models.ForeignKey(
        Event, related_name="registrations", on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="event_registrations", on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensures a user can't register twice
        unique_together = ("event", "user")

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
