from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(initial="Sonam", help_text="Yaha per naam Likhe")
