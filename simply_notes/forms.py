from django import forms 
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note


USER_TYPES = (
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )

class SignupForm(UserCreationForm):
    
    USER_TYPES = (
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),
    )
    email = forms.EmailField(max_length=200, help_text='Required')

    user_type = forms.ChoiceField(choices=USER_TYPES)
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) 
    user_type = forms.ChoiceField(choices=USER_TYPES)
    
    
#Notes Upload Form
    
class NoteUploadForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'category', 'description', 'file']