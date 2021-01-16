from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

    # This is how you can add your own custom validation for a custom field
    def clean_name(self):
        valname = self.cleaned_data['name']
        if len(valname)<4:
            raise forms.ValidationError('Enter more than or equal to 4 Char')
