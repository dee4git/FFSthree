# Generated by Django 3.1.7 on 2021-04-06 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0037_auto_20210403_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
