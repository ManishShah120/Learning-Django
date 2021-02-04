from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    # objects = models.Manager()
    students = models.Manager()
