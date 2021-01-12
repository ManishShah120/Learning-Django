# URL Dispatcher or URL Pattern inside Application in Django
## URL Pattern inside Application
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include('course.urls')),
    path('fees/', include('fees.urls')),
]
```
### Video No.: 18
