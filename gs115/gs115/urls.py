from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homefun/', views.homefun, name='homefun'),
    path('homecl/', views.HomeClassView.as_view(), name='homecl'),
    path('aboutfun/', views.aboutfun, name='aboutfun'),
    path('aboutcl/', views.AboutClassView.as_view(), name='aboutcl'),
    path('contactfun/', views.contactfun, name='contcatfun'),
    path('contactcl/', views.ContactClassView.as_view(), name='contcatcl'),
    # path('newsfun/', views.newsfun, name='newsfun'),
    path('newsfun/', views.newsfun, {'template_name' :'school/news.html'}, name='newsfun'),
    path('newsfun1/', views.newsfun, {'template_name' :'school/news1.html'}, name='newsfun'),
    # path('newscl/', views.NewsClassView.as_view(), name='newscl'),
    path('newscl/', views.NewsClassView.as_view(template_name='school/news.html'), name='newscl'),
    path('newscl1/', views.NewsClassView.as_view(template_name='school/news1.html'), name='newscl1'),
]
