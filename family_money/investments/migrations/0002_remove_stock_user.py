# Generated by Django 5.0.4 on 2024-09-16 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='user',
        ),
    ]
