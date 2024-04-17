from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    
    email= forms.EmailField(max_length=254)
    
    
    class Meta:
        model  = CustomUser
        fields = ('username','email','password1','password2')
class DonorRegistrationForm(RegistrationForm):
    # Add donor-specific fields here
    # For example:
    occupation = forms.CharField(max_length=100)
    # Add more fields as needed

    class Meta(RegistrationForm.Meta):
        fields = RegistrationForm.Meta.fields + ('occupation',)

class AssociationRegistrationForm(RegistrationForm):
    # Add association-specific fields here
    # For example:
    organization_name = forms.CharField(max_length=100)
    # Add more fields as needed

    class Meta(RegistrationForm.Meta):
        fields = RegistrationForm.Meta.fields + ('organization_name',)