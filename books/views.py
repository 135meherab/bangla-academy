from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Books
from reviews.froms import ReviewForm
from borrow.models import Borrow
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class BookDetailView(LoginRequiredMixin,DetailView):
    model = Books
    template_name = 'books/book_details.html'
    pk_url_kwarg = 'id'

    def post(self, *args, **kwargs):
        reveiw_form = ReviewForm(self.request.POST)
        book = self.get_object()
        is_borrow = Borrow.objects.filter(user = self.request.user, book=book).exists()
        if reveiw_form.is_valid() and is_borrow:
            review = reveiw_form.save(commit=False)
            review.book = book
            review.user = self.request.user
            review.save()
        return self.get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        # reviews = book.review.all()
        reveiw_form = ReviewForm()
        context["review_form"] = reveiw_form
        # context['reviews'] = reviews
        return context
    

    