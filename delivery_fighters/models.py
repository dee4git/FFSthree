import uuid

from django.contrib.auth.models import User
from django.db import models
from enrolments.models import ExtendedUser, Enrolment
from stores.models import Store

# Create your models here.

genders = [('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')]
locations = [('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Moghbazar', 'Moghbazar'), ('Badda', 'Badda'),
             ('Uttara', 'Uttara'), ('Azampur', 'Azampur'), ('Khilkhet', 'Khilkhet'), ('Banani', 'Banani'),
             ('Nilkhet', 'Nilkhet'), ('Bashabo', 'Bashabo'), ('Rampura', 'Rampura'), ('Mouchak', 'Mouchak'),
             ('Mugdha', 'Mugdha'), ('Wari', 'Wari'), ('Shahabagh', 'Shahabagh')]


class DeliveryFighter(models.Model):
    user = models.OneToOneField(ExtendedUser, default=None, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, related_name='store', blank=True, null=True, default=None,
                              on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)


class FighterRequest(models.Model):
    requester = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    fighter = models.ForeignKey(DeliveryFighter, default=None, on_delete=models.CASCADE)
    store_request = models.ForeignKey(Store, related_name='store_request', default=None, on_delete=models.CASCADE)


class Meal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    enrolment = models.ForeignKey(Enrolment, default=None, on_delete=models.CASCADE)
