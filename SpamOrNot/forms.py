from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signupform(UserCreationForm):
    first_name=forms.CharField(max_length=15, required=True, label='phone_number')
    email=forms.EmailField(required=False)
    
CHOICES =(
    ("1", "No"),
    ("2", "YES"),
)
class contactform(forms.Form):
    name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=15)
    isspam = forms.ChoiceField(choices= CHOICES)
