# Generated by Django 3.1.7 on 2021-04-03 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0036_delete_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooddetail',
            name='category',
            field=models.CharField(choices=[('Fish', 'Fish'), ('Rice', 'Rice'), ('Dal', 'Dal'), ('Meat', 'Meat'), ('Vegetable', 'Vegetable'), ('Desert', 'Desert'), ('Special', 'Special')], max_length=1000),
        ),
    ]