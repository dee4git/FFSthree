from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from stores.models import Plan

locations = [('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Moghbazar', 'Moghbazar'), ('Badda', 'Badda'),
             ('Uttara', 'Uttara'), ('Azampur', 'Azampur'), ('Khilkhet', 'Khilkhet'), ('Banani', 'Banani'),
             ('Nilkhet', 'Nilkhet'), ('Bashabo', 'Bashabo'), ('Rampura', 'Rampura'), ('Mouchak', 'Mouchak'),
             ('Mugdha', 'Mugdha'), ('Wari', 'Wari'), ('Shahabagh', 'Shahabagh')]


# Create your models here.
class ExtendedUser(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11, default='01301500600')
    location = models.CharField(choices=locations, max_length=200)
    address = models.CharField(max_length=200, default='House No / Road Number / Floor Number')
    height = models.FloatField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    bmi = models.FloatField(blank=True, null=True)
    balance = models.FloatField(default=0.0, blank=True, null=True)
    photo = models.ImageField(upload_to='pics/users', default='dp.png')


class Enrolment(models.Model):
    user = models.ForeignKey(ExtendedUser, default=None, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, default=None, on_delete=models.CASCADE)
    start_date = models.DateField()
    duration = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(100)])
    special_note = models.CharField(default='Call my brother if I dont pick up', max_length=500)
    pause = models.BooleanField(default=False)

