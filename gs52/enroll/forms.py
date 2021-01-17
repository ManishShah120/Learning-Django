from django import forms
from django.forms import widgets
from .models import User

class StudentRegistration(forms.ModelForm):

  class Meta:
      model = User
      fields = ['name', 'password', 'email']
      labels = {'name': 'Enter Name', 'password': 'Enter Password', 'email': 'Enter Email'}
      widgets = {'password':forms.PasswordInput}
