# Generated by Django 4.1 on 2023-01-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birthday', models.DateField(default='1994-09-07')),
                ('email', models.EmailField(db_index=True, max_length=254)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]