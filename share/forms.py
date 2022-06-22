from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class SignUpForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'First Name',
                                                               'class':'form-control',
                                                               }))
    
    last_name = forms.CharField(max_length=30,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'Last Name',
                                                               'class':'form-control',
                                                               }))
    
    username = forms.CharField(max_length=30,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'Username',
                                                               'class':'form-control',
                                                               }))
    
    email = forms.EmailField(required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'Email Address',
                                                               'class':'form-control',
                                                               }))
    
    password1 = forms.CharField(max_length=50,
                                 required=True,
                                 widget=forms.PasswordInput(attrs={'placeholder':'Password',
                                                               'class':'form-control',
                                                               'data-toggle':'password',
                                                               'id':'password',
                                                               }))
    password2 = forms.CharField(max_length=50,
                                 required=True,
                                 widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password',
                                                               'class':'form-control',
                                                               'data-toggle':'password',
                                                               'id':'password',
                                                               }))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder':'Username',
                                                             'class':'form-control'
                                                             }))
    password1 = forms.CharField(max_length=50,
                                 required=True,
                                 widget=forms.PasswordInput(attrs={'placeholder':'Password',
                                                               'class':'form-control',
                                                               'data-toggle':'password',
                                                               'id':'password',
                                                               'name':'password',
                                                               }))
    
    
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
class UpdateProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols':10}))

    class Meta:
        model = Profile
        fields = ['photo', 'bio']


    
class UpdateUserForm(UserCreationForm):
    username = forms.CharField(max_length=30,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'Username',
                                                               'class':'form-control',
                                                               }))
    
    email = forms.EmailField(required=True,
                                 widget=forms.TextInput(attrs={'placeholder':'Email Address',
                                                               'class':'form-control',
                                                               }))
    
    class Meta:
        model = User
        fields = ['username', 'email']