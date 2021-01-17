from django import forms
from django.forms import widgets
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['name', 'email', 'password']
        # If you want to change the order of the fields then simply change the orders in `fields`
        fields = ['name', 'password', 'email']
