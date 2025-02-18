from django.db import models


class Event(models.Model):
    EVENT_TYPES = (
        ('RAMADAN', 'Ramadan Welcome'),
        ('NEW_STUDENT', 'New Entrants Welcome'),
        ('BOOK_REVIEW', 'Book Review'),
        ('FUN_DAY', 'Fun Day'),
    )
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    attendees = models.ManyToManyField(
        'accounts.CustomUser', through='EventRegistration')


class EventRegistration(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
