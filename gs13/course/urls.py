from django.contrib import admin
from django.urls import path
from .views import learn_django

urlpatterns = [
    path('learndj/', learn_django),
]
