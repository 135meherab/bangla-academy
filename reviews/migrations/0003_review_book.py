# Generated by Django 4.2.7 on 2024-01-09 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_books_review'),
        ('reviews', '0002_remove_review_email_remove_review_name_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.books'),
        ),
    ]