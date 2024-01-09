from django.contrib import admin
from .models import Category
# Register your models here.
class AdminCategorySlug(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_displayed = ['name', 'slug']

admin.site.register(Category, AdminCategorySlug)