# Generated by Django 2.2 on 2021-03-25 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0021_fooddetail_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooddetail',
            name='store',
        ),
    ]
