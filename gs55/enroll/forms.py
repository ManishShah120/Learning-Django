from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['name', 'password', 'email']
        # fields = '__all__'
        exclude = ('name', )
