from django.db import models
from categories.models import Category

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    imange = models.ImageField(upload_to='books/media/uploads/')
    borrowing_price = models.IntegerField()
    category = models.ManyToManyField(Category)
    
