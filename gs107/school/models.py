from django.db import models
from .managers import CustomManager

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    # objects = models.Manager()
    students = CustomManager()
