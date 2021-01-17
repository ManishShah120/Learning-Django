from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Password(again)' ,widget=forms.PasswordInput)

    def clean(self):
        # The call to super().clean() ensures that any validation logic in parent classes is maintained.
        cleaned_data = super().clean()
        valpwd = cleaned_data['password']
        valrpwd = cleaned_data['rpassword']
        if valpwd != valrpwd:
            raise forms.ValidationError('Not Matching Password')
