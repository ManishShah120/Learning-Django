from django.contrib import admin
from django.urls import path
from course import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learndj/', views.learn_django),
    path('learnpy', views.learn_python),
    path('learnnv/', views.learn_var),
    path('learnm/', views.learn_math),
    path('learnf/', views.learn_format),
]
