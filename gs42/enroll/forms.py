from django import forms
from django.core import validators

class StudentRegistration(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    email = forms.EmailField()
