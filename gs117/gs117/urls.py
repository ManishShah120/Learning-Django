from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplateView.as_view(template_name='school/home.html'), name='blankhome'),
    path('home/', views.RedirectView.as_view(url='/'), name='home'),

    # path('index/', views.RedirectView.as_view(url='/'), name='index'),
    path('index/', views.RedirectView.as_view(pattern_name='home'), name='index'),

    # path('geekyshows/', views.RedirectView.as_view(url='https://www.geekyshows.com'), name='go-to-geekyshows'),
    path('geekyshows/', views.GeekyShowsRedirectView.as_view(), name='go-to-geekyshows'),

    path('home/<int:pk>/', views.GeekRedirectView.as_view(), name='geek'),
    path('roll/<int:pk>/', views.TemplateView.as_view(template_name='school/home.html'), name='mindex'),

    # path('home/<slug:post>/', views.GeekRedirectView.as_view(), name='geek'),
    # path('<slug:post>/', views.TemplateView.as_view(template_name='school/home.html'), name='mindex'),
]
