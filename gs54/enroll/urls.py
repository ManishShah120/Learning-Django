from django.urls import path, register_converter
from .views import show_details
from . import converters

register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('session/<yyyy:year>', show_details, name='detail'),
]
