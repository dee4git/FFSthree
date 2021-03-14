from django.db import models
from django.contrib.auth.models import User
locatoins = [('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Moghbazar', 'Moghbazar'), ('Badda', 'Badda'),
             ('Uttara', 'Uttara'), ('Azampur', 'Azampur'), ('Khilkhet', 'Khilkhet'), ('Banani', 'Banani'),
             ('Nilkhet', 'Nilkhet'), ('Bashabo', 'Bashabo'), ('Rampura', 'Rampura'), ('Mouchak', 'Mouchak'),
             ('Mugdha', 'Mugdha'), ('Wari', 'Wari'), ('Shahabagh', 'Shahabagh')]


# Create your models here.
class Store(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(default="Name", max_length=100)
    phone = models.CharField(max_length=11, default='01719500600', blank=False, null=False)
    description = models.CharField(default="This is the description area...", max_length=1000, blank=True, null=True)
    location = models.CharField(choices=locatoins, max_length=200)
    display_picture = models.ImageField(upload_to='pics/stores')



