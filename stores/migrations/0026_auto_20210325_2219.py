# Generated by Django 2.2 on 2021-03-25 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0025_auto_20210325_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooddetail',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stores.Store'),
        ),
    ]
