from django.shortcuts import render
from django.views.generic.base import TemplateView
from books.models import Books
from categories.models import Category
# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_books = Books.objects.all()
        all_categories = Category.objects.all()
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category_name = Category.objects.get(slug = category_slug)
            all_books = Books.objects.filter(category = category_name)

        context['all_books'] = all_books 
        context['all_categories'] = all_categories
        return context