# Generated by Django 3.1.7 on 2021-03-28 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrolments', '0010_auto_20210329_0218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrolment',
            name='daily_meal_count',
        ),
        migrations.AddField(
            model_name='enrolment',
            name='day_meal_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='enrolment',
            name='night_meal_count',
            field=models.IntegerField(default=1),
        ),
    ]
