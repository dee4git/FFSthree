# Generated by Django 2.2 on 2021-03-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0033_auto_20210326_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='visibility',
            field=models.IntegerField(default=0),
        ),
    ]
