from typing import SupportsRound
from django.contrib import admin
from .models import Sutdent

# Register your models here.

# One Way
# admin.site.register(Sutdent)

# Second Way
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'stuid', 'stuname', 'stuemail', 'stupass')

# admin.site.register(Sutdent, StudentAdmin)

# Third Way
@admin.register(Sutdent)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stuid', 'stuname', 'stuemail', 'stupass')
