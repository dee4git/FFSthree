# Generated by Django 3.1.7 on 2021-04-03 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_fighters', '0007_auto_20210401_0307'),
        ('enrolments', '0011_auto_20210329_0219'),
        ('rates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(choices=[(1.0, 1.0), (2.0, 2.0), (3.0, 3.0), (4.0, 4.0), (5.0, 5.0)], default=5.0, max_length=200)),
                ('comment', models.TextField(default='How was your meal today?', max_length=1000)),
                ('enroller', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='enrolments.extendeduser')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery_fighters.meal')),
            ],
        ),
    ]