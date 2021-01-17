from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
