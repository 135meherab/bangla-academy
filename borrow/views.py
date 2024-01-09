
from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from books.models import Books
from .models import Borrow
from wallet.models import Wallet
from django.views.generic.list import ListView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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
def BorrowBook(request, id):
    book = Books.objects.get(id=id)
    wallet = Wallet.objects.get(user = request.user)
    if wallet.balance >= book.borrowing_price:
        Borrow.objects.create(book=book, user = request.user)
        wallet.balance -= book.borrowing_price
        wallet.save()
        messages.success(request,'You have borrowed the book Successfully')
        send_mail(request.user, book.borrowing_price, 'Book borrowed', 'borrow/borrow_mail.html')
    else:
         messages.error(request,"Your don not have enough balance. first recharge your wallet")
    return redirect('index')


class BorrowedHistoryView(LoginRequiredMixin,ListView):
    template_name = 'borrow/borrow_report.html'
    model = Borrow

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            user = self.request.user
        )
        return queryset
    
@login_required(login_url="login")
def ReturnBook(request, id):
    book = Books.objects.get(id=id)
    wallet = Wallet.objects.get(user = request.user)
    wallet.balance += book.borrowing_price
    wallet.save()

    borrow = Borrow.objects.get(user=request.user, book=book)
    borrow.is_retuened = True
    borrow.save()
    messages.success(request,'We have received the book. Theank you for returning the book. borrowed amount is added to your wallet')
    return redirect('borrowed_history')
