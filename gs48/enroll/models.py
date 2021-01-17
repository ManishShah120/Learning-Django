from django.db import models

# Create your models here.
class User(models.Model):
    # To change the required field from simpley add `blank=True`
    # name = models.CharField(max_length=70, blank=True)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)