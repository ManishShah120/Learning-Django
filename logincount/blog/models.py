from django.db import models

# Post Model
class Post(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()

# Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=200)
