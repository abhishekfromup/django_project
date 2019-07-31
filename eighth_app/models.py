from django.db import models

# Create your models here.

class StudentFeedback(models.Model):
    name = models.CharField(max_length = 30)
    course = models.CharField(max_length = 30)
    email = models.EmailField()
    feedback = models.CharField(max_length = 150)