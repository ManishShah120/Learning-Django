from django.contrib import admin
from django.urls import path, include
from .views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('course/', include('course.urls')),
    path('fees/', include('fees.urls')),
]
