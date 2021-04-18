from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	first_name=forms.CharField(max_length=100,required=True)
	last_name=forms.CharField(max_length=100,required=True)
	username=forms.CharField(max_length=100,required=True)
	password1=forms.PasswordInput()
	password2=forms.PasswordInput()
	email=forms.EmailField(max_length=254,help_text='eg. yourmail@anymail.com',required=True)

	class Meta:
		model=User
		fields=('first_name','last_name','username','email','password1','password2')