# Generated by Django 5.0.4 on 2024-09-16 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financials', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='user',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='user',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='user',
        ),
        migrations.RemoveField(
            model_name='income',
            name='user',
        ),
        migrations.RemoveField(
            model_name='savingsgoal',
            name='user',
        ),
    ]
