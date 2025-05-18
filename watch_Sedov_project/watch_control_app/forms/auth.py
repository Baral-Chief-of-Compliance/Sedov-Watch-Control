from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class AuthForm(AuthenticationForm):
    """Форма аунтификации"""
    username = forms.CharField(widget=TextInput(attrs={'class':'form-control','placeholder':'Логин'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'Пароль'}))

    def confirm_login_allowed(self, user):
        return super().confirm_login_allowed(user)