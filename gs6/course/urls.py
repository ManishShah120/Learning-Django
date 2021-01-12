from django.contrib import admin
from django.urls import path
from .views import learn_django, learn_python

urlpatterns = [
    path('learndj/', learn_django),
    path('learnpy/', learn_python),
]
