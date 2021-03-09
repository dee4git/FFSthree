from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from stores.models import Store

choice = [(1.0, 1.0), (2.0, 2.0), (3.0, 3.0), (4.0, 4.0), (5.0, 5.0)]


class StoreRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    rating = models.FloatField(max_length=200, choices=choice, default=5.0)
    comment = models.TextField(max_length=1000, default="Share You experience")