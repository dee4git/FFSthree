# Generated by Django 3.1.7 on 2021-04-03 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_fighters', '0007_auto_20210401_0307'),
        ('rates', '0003_mealrating_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealrating',
            name='meal',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='delivery_fighters.meal'),
        ),
    ]