from django.db import models
from django.conf import settings  # Import settings to access AUTH_USER_MODEL

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Donation(models.Model):
    donor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use AUTH_USER_MODEL
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    donated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor.username} - {self.amount}"

class CharityVisit(models.Model):
    organization = models.CharField(max_length=200)
    date = models.DateField()
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)  # Use AUTH_USER_MODEL