from django.contrib import admin
from django.urls import path
from course import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learndj/', views.learn_django),
    path('altlearndj/', views.learn_django),
]
