from django.db import models
from django.contrib.auth.models import User
from books.models import Books
# Create your models here.
class Review(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null = True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE, blank=True, null = True)