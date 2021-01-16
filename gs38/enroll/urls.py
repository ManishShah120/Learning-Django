from django.urls import path, include
from . import views

urlpatterns = [
    path('stu/', views.showformdata, name='studetails'),
    path('success/', views.thankyou, name='success'),
]
