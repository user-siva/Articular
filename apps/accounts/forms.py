from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm
from django import forms

class LoginForm(LoginForm):
 
    def signup(self, request, user):
        user.save()
        return user