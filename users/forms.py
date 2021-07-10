from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class NewUserForm(ModelForm):
    class Meta:
        model = NewUser
        fields = ['user_name', 'email', 'first_name', 'last_name', 'referral_code', 'bitcoin_wallet_address',
                  'phone_number','next_of_kin', 'next_of_kin_phone_number','password']