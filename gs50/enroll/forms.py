from django import forms
from django.forms import widgets
from .models import User

class StudentRegistration(forms.ModelForm):
  # To apply an extra Validators to `Name` Higer Priority is given to this than the Model
  name = forms.CharField(max_length=50, required=False)
 
  class Meta:
      model = User
      fields = ['name', 'password', 'email']
      labels = {'name': 'Enter Name', 'password': 'Enter Password', 'email': 'Enter Email'}
      widgets = {'password':forms.PasswordInput}
