# Generated by Django 4.2.7 on 2023-12-10 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.author'),
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book'),
        ),
    ]
