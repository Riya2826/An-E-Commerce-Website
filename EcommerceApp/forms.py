from django.forms import ModelForm
from django import forms
from .models import Registereduser

class Registerform(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Registereduser
        fields = '__all__'
        labels =  {
            "name": "Username",
            "emailid": "Email Id",
            "phnnum": "Phone Number",
            "password": "Password"}


    
        