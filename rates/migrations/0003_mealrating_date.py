# Generated by Django 3.1.7 on 2021-04-03 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0002_mealrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealrating',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
