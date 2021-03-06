from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, )
    last_name = forms.CharField(max_length=30, )
    email = forms.EmailField(max_length=100, )
    username = forms.CharField(max_length=50)
    password1 = forms.CharField(widget=forms.PasswordInput, min_length=8)
    password2 = forms.CharField(widget=forms.PasswordInput, min_length=8)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


# Profile Form
class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
