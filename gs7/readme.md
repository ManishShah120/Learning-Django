# URL Dispatcher or URL Pattern inside Application in Django
## URL Pattern inside Application(Second & Third Way)
### Second Method Video 18
```
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
```
