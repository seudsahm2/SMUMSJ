from django.db import models
from django.utils import timezone


class Hadith(models.Model):
    text = models.TextField()
    reference = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now, unique=True)

    def __str__(self):
        return f"Hadith for {self.date}"


class ScholarLecture(models.Model):
    title = models.CharField(max_length=200)
    scholar = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    video_url = models.URLField()
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.title} by {self.scholar}"


class Question(models.Model):
    user = models.ForeignKey('accounts.CustomUser',
                             on_delete=models.SET_NULL, null=True, blank=True)
    question = models.TextField()
    answer = models.TextField(blank=True)
    asked_on = models.DateTimeField(auto_now_add=True)
    answered_on = models.DateTimeField(null=True, blank=True)
    is_public = models.BooleanField(default=False)

    class Meta:
        ordering = ['-asked_on']

    def __str__(self):
        return f"Question from {self.user} on {self.asked_on.date()}"
