from django.urls import path
from .views import show_details, home, show_subdetails


urlpatterns = [
    path('', home, {'check': 'OKashbjsadhfbmd'}, name='home'),
    path('<int:my_id>/', show_details, name='detail'),
    path('<int:my_id>/<int:my_subid>', show_subdetails, name='subdetail'),
]
