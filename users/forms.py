# -*- coding: utf-8 -*-

from django import forms


class LoginForm(forms.Form):

    usr = forms.CharField(label="Nombre de Usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class RegisterForm(forms.Form):

    email = forms.EmailField(label="Dirección de Correo Electronico", required=True)
    user = forms.CharField(label="Nombre de Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

