# ramadan/models.py (new app)
from django.db import models
from accounts.models import CustomUser


class RamadanChecklist(models.Model):
    DAY_CHOICES = [(i, f"Day {i}") for i in range(1, 31)]
    day = models.IntegerField(choices=DAY_CHOICES, unique=True)
    task = models.TextField()
    verse = models.TextField(blank=True)


class UserProgress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    day = models.ForeignKey(RamadanChecklist, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
