# Generated by Django 3.1.7 on 2021-03-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enrolments', '0002_auto_20210328_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='bmi',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]