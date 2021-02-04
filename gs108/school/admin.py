from django.contrib import admin
from .models import Student, ProxyStudent

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']


@admin.register(ProxyStudent)
class ProxyStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']
