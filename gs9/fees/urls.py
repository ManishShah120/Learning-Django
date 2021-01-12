from django.contrib import admin
from django.urls import path
from .views import fees_django, fees_python

urlpatterns = [
    path('feesdj/', fees_django),
    path('feespy/', fees_python),
]
