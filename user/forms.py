from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class SigninForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class ProfileForm(forms.ModelForm ):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Full Name'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter Your Address'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter Few Lines About Yourself'}))
    phone = forms.IntegerField(widget=forms.NumberInput)
   
    class Meta:
        model=models.UserProfile
        fields=['name','about','phone','address','profile_pic']