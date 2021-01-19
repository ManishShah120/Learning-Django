from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms


class SignUpForm(UserCreationForm):
    # To overwrite the label of the `password confirmation`
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        # To change the default `email` field name
        labels = {'email': 'Email'}

# We will also need to work with the UserCreationForm as it has many unwanted data
class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_active'] # Whatever you need to show in the profile page add that in this list
        labels = {'email': 'Email'}
