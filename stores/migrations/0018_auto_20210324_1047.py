# Generated by Django 2.2 on 2021-03-24 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0017_plan_visibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='photo_1',
            field=models.ImageField(default='plan.png', upload_to='pics/plans'),
        ),
        migrations.AddField(
            model_name='plan',
            name='photo_2',
            field=models.ImageField(default='plan.png', upload_to='pics/plans'),
        ),
        migrations.AddField(
            model_name='plan',
            name='photo_3',
            field=models.ImageField(default='plan.png', upload_to='pics/plans'),
        ),
        migrations.AddField(
            model_name='plan',
            name='photo_4',
            field=models.ImageField(default='plan.png', upload_to='pics/plans'),
        ),
    ]
