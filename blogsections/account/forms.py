from django import forms

"""
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=22, label="Username")
    password = forms.CharField(max_length=22, label="Password", widget=forms.PasswordInput)

"""

class SingUpForm(forms.Form):
    username = forms.CharField(max_length=22, label="Username ")
    email = forms.EmailField( label="e-mail   ")
    password1 = forms.CharField(max_length=22, label="Password1", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=22, label="Password2", widget=forms.PasswordInput)
