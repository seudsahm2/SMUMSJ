# resources/models.py
from django.db import models

ISLAMIC_CATEGORIES = (
    ('QURAN', 'Quran Studies'),
    ('HADITH', 'Hadith'),
    ('FIQH', 'Islamic Jurisprudence'),
    ('HISTORY', 'Islamic History'),
)


class IslamicResource(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=ISLAMIC_CATEGORIES)
    description = models.TextField()
    file = models.FileField(upload_to='resources/')
    thumbnail = models.ImageField(upload_to='resource_thumbs/')
    upload_date = models.DateTimeField(auto_now_add=True)
    downloads = models.PositiveIntegerField(default=0)
