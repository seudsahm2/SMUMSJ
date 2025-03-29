# education/models.py
from django.db import models
from django.contrib.auth.models import User  # Import the default User model


class EducationalResource(models.Model):
    SUBJECTS = (
        ('MATH', 'Mathematics'),
        ('SCIENCE', 'Science'),
        ('HISTORY', 'History'),
    )
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=10, choices=SUBJECTS)
    file = models.FileField(upload_to='education/resources/')
    upload_date = models.DateTimeField(auto_now_add=True)


class TutorRequest(models.Model):
    student = models.ForeignKey(
        User, related_name='student_requests', on_delete=models.CASCADE)
    tutor = models.ForeignKey(User,
                              related_name='tutor_assignments', null=True, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    status = models.CharField(max_length=11, default='OPEN', choices=[
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('CLOSED', 'Closed')
    ])
