# Generated by Django 3.1.7 on 2021-03-31 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0036_delete_food'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enrolments', '0011_auto_20210329_0219'),
        ('delivery_fighters', '0002_auto_20210331_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryFighter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_available', models.BooleanField(default=True)),
                ('store', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='store', to='stores.store')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='enrolments.extendeduser')),
            ],
        ),
        migrations.CreateModel(
            name='FighterRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fighter', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='delivery_fighters.deliveryfighter')),
                ('requester', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('store_request', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='store_request', to='stores.store')),
            ],
        ),
    ]
