from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    
    email= forms.EmailField(max_length=254)
    
    
    class Meta:
        model  = CustomUser
        fields = ('username','email','password1','password2', 'is_donor', 'is_association')
