from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app1.models import *
class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')
        
class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['mobile','gender','country']

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','brand', 'colour', 'price', 'quantity','description')