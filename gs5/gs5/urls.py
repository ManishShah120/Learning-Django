from django.contrib import admin
from django.urls import path
from course.views import learn_django
from fees.views import fees_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learndj/', learn_django),
    path('feedj/', fees_django),
]
