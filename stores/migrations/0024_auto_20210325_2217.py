# Generated by Django 2.2 on 2021-03-25 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0023_fooddetail_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooddetail',
            name='store',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='stores.Store'),
        ),
    ]
