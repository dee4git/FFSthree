from django.contrib.auth.models import User
from django.db import models

# Create your models here.

genders = [('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')]
locations = [('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Moghbazar', 'Moghbazar'), ('Badda', 'Badda'),
             ('Uttara', 'Uttara'), ('Azampur', 'Azampur'), ('Khilkhet', 'Khilkhet'), ('Banani', 'Banani'),
             ('Nilkhet', 'Nilkhet'), ('Bashabo', 'Bashabo'), ('Rampura', 'Rampura'), ('Mouchak', 'Mouchak'),
             ('Mugdha', 'Mugdha'), ('Wari', 'Wari'), ('Shahabagh', 'Shahabagh')]


class DeliveryFighter(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default=None)
    gender = models.CharField(max_length=100, choices=genders)
    phone = models.CharField(max_length=11, default='01719600900')
    preferred_location = models.CharField(choices=locations, max_length=100)
    photo = models.ImageField(upload_to='pics/delivery_fighters', default='dp.png')
    is_available = models.BooleanField(default=True)
    balance = models.FloatField(default=0.0)
