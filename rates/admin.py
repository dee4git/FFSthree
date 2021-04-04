from django.contrib import admin

# Register your models here.
from .models import StoreRating, MealRating
admin.site.register(StoreRating)
admin.site.register(MealRating)
