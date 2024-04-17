from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User  # Add this line
from .models import Donor, Association

class DonorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['username', 'email', 'password',]  # Add fields as needed

class AssociationRegistrationForm(forms.ModelForm):
    class Meta:
        model = Association
        fields = ['username', 'email', 'password',]



class RegistrationForm(UserCreationForm):
    
    email= forms.EmailField(max_length=254)
    
    
    class Meta:
        model  = User
        fields = ('username','email','password1','password2')
