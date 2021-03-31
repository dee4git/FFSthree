from django.contrib import admin

# Register your models here.
from .models import DeliveryFighter, FighterRequest, Meal
admin.site.register(DeliveryFighter)
admin.site.register(FighterRequest)
admin.site.register(Meal)

