from django.db import models
from django.contrib.auth.models import User
from books.models import Books
# Create your models here.
class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_retuened = models.BooleanField(default=False)

    def __str__(self):
        return self.book.title