from django.contrib import admin

# Register your models here.
from .models import DeliveryFighter, FighterRequest
admin.site.register(DeliveryFighter)
admin.site.register(FighterRequest)

