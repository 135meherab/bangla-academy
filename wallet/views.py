from django.shortcuts import render, redirect
from .forms import WalletRechargeForm
from .models import Wallet
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

# Create your views here.
def send_mail(user, amount, subject, template):
    sub = subject
    msg = render_to_string(template,{
        'user': user,
        'amount': amount
    })
    send_mail = EmailMultiAlternatives(sub,'', to=[user.email])
    send_mail.attach_alternative(msg, 'text/html')
    send_mail.send()

@login_required(login_url="login")
def RechargeWallet(request):
    if request.method == 'POST':
        form = WalletRechargeForm(request.POST)
        if form.is_valid():
            wallet, create = Wallet.objects.get_or_create(user = request.user)
            amount = form.cleaned_data['amount']
            wallet.balance += amount
            wallet.save()
            messages.success(request,f'{amount} added to wallet')
            send_mail(request.user, amount, 'Wallet Recharge','wallet/recharge_mail.html')
            return redirect('index')
    else:
        form = WalletRechargeForm()
    return render(request, 'wallet/recharge.html')