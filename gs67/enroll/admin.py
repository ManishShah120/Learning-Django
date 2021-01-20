from django.contrib import admin
from .models import Blog

# Register your models here.
@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']
