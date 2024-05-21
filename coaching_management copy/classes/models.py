# classes/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    fees = models.DecimalField(max_digits=10, decimal_places=2)
    faculty_name = models.CharField(max_length=255)  # New field
    duration = models.CharField(max_length=50)  # New field

    def __str__(self):
        return self.name

class Registration(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_student': True})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.username} - {self.course.name}'
