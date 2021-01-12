from django.contrib import admin
from django.urls import path
from course import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learndj/', views.learn_django),
    path('learnpy/', views.learn_python),
    path('learnvar/', views.learn_var),
    path('learnmath/', views.learn_math),
    path('learnformat/', views.learn_format),
    path('', views.index),
]
