from django.db import models
from django.contrib.auth.models import User

# Page class
class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()


class Like(Page):
    panna = models.OneToOneField(Page, on_delete=models.CASCADE, primary_key=True, parent_link=True)  # panna means page
    likes = models.IntegerField()
