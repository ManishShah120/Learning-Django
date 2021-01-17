from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        if len(valname) < 4:
            raise forms.ValidationError('Name should contain more than or equal to 4 Char')
        
        if len(valemail) < 4:
            raise forms.ValidationError('Email should contain more than 10 char')
