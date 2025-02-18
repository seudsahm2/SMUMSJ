from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLES = (
        ('AMIR', 'Amir'),
        ('MEMBER', 'Member'),
        ('GUEST', 'Guest'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='GUEST')
    phone = models.CharField(max_length=20, blank=True)
    is_verified = models.BooleanField(default=False)

    def is_amir(self):
        return self.role == 'AMIR'
