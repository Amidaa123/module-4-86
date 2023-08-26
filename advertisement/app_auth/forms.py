from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm):

    username = forms.CharField(
        label="Username",
        min_length=5,
        max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"})
    )
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"})
        )
    surname = forms.CharField(
        label="Surname",
        widget=forms.TextInput(attrs={"class": "form-control form-control-lg"})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg"})
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg"})
    )
