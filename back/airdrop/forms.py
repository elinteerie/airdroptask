# airdrop/forms.py

from django import forms
from .models import User

class AirdropForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['solana_wallet', 'telegram_username', 'quote_retweet_link']

class UserForm(forms.ModelForm):
    class Meta:
        model =User
        fields = ['solana_wallet']