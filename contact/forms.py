from django import forms
from .models import ContactMessage
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=("username","email","password1","password2")

class LoginForm(AuthenticationForm):
    username=forms.CharField(label="Username or Email")
    password=forms.CharField(widget=forms.PasswordInput)

class ContactForm(forms.ModelForm):
    class Meta:
        model=ContactMessage
        fields=['name','email','message']
