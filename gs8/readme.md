# URL Dispatcher or URL Pattern inside Application in Django
## URL Pattern inside Application(Third Way)
### Third Method Video 18
```
coursepatterns = [
        path('learndj/', learn_django),
        path('learnpy/', learn_python),
]

feespattern = [
        path('feesdj/', fees_django),
        path('feespy/', fees_python),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include(coursepatterns)),
    path('fees/', include(feespattern))
]
```
