from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm
from django import forms

class SignupForm(SignupForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

 
    def signup(self, request, user):
        user.save()
        return user