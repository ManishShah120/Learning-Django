from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set/', views.settestcookie),
    path('check/', views.checktestcookie),
    path('del/', views.deltestcookie),
]
