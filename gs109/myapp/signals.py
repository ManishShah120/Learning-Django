from django.db import models
from .models import Page
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Page)
def delete_related_user(sender, instance, **kwargs):
    # print("Page Post_Delete")
    instance.user.delete()
