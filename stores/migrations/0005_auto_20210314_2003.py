# Generated by Django 2.2 on 2021-03-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_auto_20210314_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.CharField(default='01719500600', max_length=11),
        ),
    ]
