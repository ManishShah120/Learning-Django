from django.contrib import admin
from django.urls import path, include
from course.views import (
    learn_django,
    learn_python,
)
from fees.views import (
    fees_django,
    fees_python,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include([
        path('learndj/', learn_django),
        path('learnpy/', learn_python),
    ])),
    path('fees/', include([
        path('feesdj/', fees_django),
        path('feespy/', fees_python),
    ]))
]
