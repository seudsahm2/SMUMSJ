from django.db import models

class Donation(models.Model):
    donor = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    campaign = models.CharField(max_length=100)
    
class CharityVisit(models.Model):
    organization = models.CharField(max_length=200)
    date = models.DateField()
    participants = models.ManyToManyField('accounts.CustomUser')