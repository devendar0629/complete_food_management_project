from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=36,widget=forms.PasswordInput)