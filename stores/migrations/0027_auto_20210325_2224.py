# Generated by Django 2.2 on 2021-03-25 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0026_auto_20210325_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooddetail',
            name='store',
        ),
        migrations.CreateModel(
            name='DetailFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Fish', 'Fish'), ('Rice', 'Rice'), ('Dal', 'Dal'), ('Meet', 'Meet'), ('Vegetable', 'Vegetable'), ('Desert', 'Desert'), ('Special', 'Special')], max_length=1000)),
                ('name', models.CharField(default='Detail Food name', max_length=100)),
                ('amount', models.CharField(default='100 g', max_length=100)),
                ('calorie', models.FloatField(default=0.0)),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stores.Store')),
            ],
        ),
    ]
