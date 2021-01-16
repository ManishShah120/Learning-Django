from django.urls import path
from .views import studentinfo

urlpatterns = [
    path('stu/', studentinfo, name='studetails'),
]
