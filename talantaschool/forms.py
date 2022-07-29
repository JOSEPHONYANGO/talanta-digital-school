from django import forms
from models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile        
        fields=['first_name', 'last_name', 'username', 'location', 'mobile_number', 'email']
        
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile        
        fields=['first_name', 'last_name', 'username', 'location', 'mobile_number', 'email']

class LoginForm(forms.Form):
    
        email=forms.CharField(max_length=50,widget=forms.EmailInput())
        password=forms.CharField(max_length=50,widget=forms.PasswordInput())  
