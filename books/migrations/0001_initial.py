# Generated by Django 4.2.7 on 2024-01-08 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('imange', models.ImageField(upload_to='books/media/uploads/')),
                ('borrowing_price', models.IntegerField()),
            ],
        ),
    ]
