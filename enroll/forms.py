from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class regi(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels={'first_name':'Enter Your Name','last_name':'Enter Your Last Name',
                'email':'Email Address'}

        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
               'first_name': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[A-Za-z]+'}),
               'last_name': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[A-Za-z]+'}),
               'email': forms.EmailInput(attrs={'class': 'form-control'})}


class log(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username']
        labels={'username':'user'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}

class profile_user(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','last_login','date_joined','is_active']


class profile_admin(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
