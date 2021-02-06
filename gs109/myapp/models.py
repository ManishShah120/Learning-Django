from django.db import models
from django.contrib.auth.models import User

# class User(models.Model) # is already created

# Page class
class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    # If user is deleted then its related page will also be deleted, and the user can only crate page if their `is_staff` status is True
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff':True})

    # # If User is deleted than its related page will not be deleted
    # user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()
