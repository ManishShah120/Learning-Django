from django.urls import path, include
from . import views

urlpatterns = [
    path('stu/', views.showformdata, name='studetails'),
]
