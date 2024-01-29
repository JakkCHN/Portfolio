from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email address', help_text='Your email address.')
    date_of_birth = forms.DateField(required=False, help_text='Your date of birth (optional)')
    address = forms.CharField(max_length=255, required=False, help_text='Your address (optional)')
    city_town = forms.CharField(max_length=100, required=False, help_text='Your city/town (optional)')
    country = forms.CharField(max_length=100, required=False, help_text='Your country (optional)')
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'date_of_birth', 'address', 'city_town', 'country']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        
class ChangePasswordForm(PasswordChangeForm):
    pass