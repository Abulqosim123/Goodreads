# Generated by Django 5.0 on 2023-12-12 15:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_bookreview_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookreview',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
