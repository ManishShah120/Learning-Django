from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    date = models.DateField()
    
    class Meta:
        abstract = True


class Student(CommonInfo):
    fees = models.IntegerField()
    date = None


class Teacher(CommonInfo):
    salary = models.IntegerField()

 
class Contractor(CommonInfo):
    date = models.DateTimeField()
    payment = models.IntegerField()






# These tables can be implemented by using Abstract Base Class Inheritance i.e., by the above way as we have implemented it
'''
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70) # Same
    age = models.IntegerField() # Same
    fees = models.IntegerField()


class Teacher(models.Model):
    name = models.CharField(max_length=70) # Same
    age = models.IntegerField() # Same
    date = models.DateField()
    salary = models.IntegerField()


class Contractor(models.Model):
    name = models.CharField(max_length=70) # Same
    age = models.IntegerField() # Same
    date = models.DateTimeField()
    payment = models.IntegerField()
'''