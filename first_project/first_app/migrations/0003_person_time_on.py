# Generated by Django 4.1 on 2023-01-24 05:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_add_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='time_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
