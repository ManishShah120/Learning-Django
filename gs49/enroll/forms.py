from django import forms
from django.forms import widgets
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['name', 'email', 'password']
        # If you want to change the order of the fields then simply change the orders in `fields`
        fields = ['name', 'password', 'email']
        labels = {'name': 'Enter Name', 'password': 'Enter Password', 'email': 'Enter Email'}
        help_text = {'name': 'Enter Your Full Name'}
        error_messages = {'name': {'required': 'Naam Likhna Jarruri hei'},
                          'password': {'required': 'Password Likhna jarrurui hei'}
                        }
        widgets = {'password':forms.PasswordInput, 
                   'name':forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'yaha naam Likhe'}),
        }
