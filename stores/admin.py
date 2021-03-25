from django.contrib import admin

# Register your models here.
from .models import Store, Food, FoodDetail, Week, Plan
admin.site.register(Store)
admin.site.register(Food)
admin.site.register(FoodDetail)
admin.site.register(Week)
admin.site.register(Plan)
