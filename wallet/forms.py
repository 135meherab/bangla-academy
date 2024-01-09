from .models import WalletRecharge
from django import forms

class WalletRechargeForm(forms.ModelForm):
    class Meta:
        model = WalletRecharge
        fields = ['amount']
        
