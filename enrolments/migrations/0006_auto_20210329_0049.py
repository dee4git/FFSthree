# Generated by Django 3.1.7 on 2021-03-28 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrolments', '0005_enrolment'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolment',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='enrolment',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
