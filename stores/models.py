from django.db import models
from django.contrib.auth.models import User

locations = [('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Moghbazar', 'Moghbazar'), ('Badda', 'Badda'),
             ('Uttara', 'Uttara'), ('Azampur', 'Azampur'), ('Khilkhet', 'Khilkhet'), ('Banani', 'Banani'),
             ('Nilkhet', 'Nilkhet'), ('Bashabo', 'Bashabo'), ('Rampura', 'Rampura'), ('Mouchak', 'Mouchak'),
             ('Mugdha', 'Mugdha'), ('Wari', 'Wari'), ('Shahabagh', 'Shahabagh')]


# Create your models here.
class Store(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(default="Name", max_length=100)
    phone = models.CharField(max_length=11, default='01719500600', blank=False, null=False)
    description = models.CharField(default="This is the description area...", max_length=1000, blank=True, null=True)
    location = models.CharField(choices=locations, max_length=200)
    display_picture = models.ImageField(upload_to='pics/stores', default='store.gif')


food_type = [('Fish', 'Fish'), ('Rice', 'Rice'), ('Dal', 'Dal'), ('Meat', 'Meat'),
             ('Vegetable', 'Vegetable'), ('Desert', 'Desert'), ('Special', 'Special')]


class FoodDetail(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, default=None)
    category = models.CharField(choices=food_type, max_length=1000)
    name = models.CharField(default='Detail Food name', max_length=100)
    amount = models.CharField(default='100 g', max_length=100)
    calorie = models.FloatField(default=0.0)


plan_category = [('Homemade', 'Homemade'), ('Professional', 'Professional')]


class Plan(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100, default='Plan Name')
    price = models.FloatField(default=0.0)
    capacity = models.IntegerField(default=10)
    category = models.CharField(choices=plan_category, max_length=100)
    total_estimated_calorie = models.FloatField(default=0.0)
    visibility = models.BooleanField(default=False)
    photo_1 = models.ImageField(upload_to='pics/plans', default='plan.png')
    photo_2 = models.ImageField(upload_to='pics/plans', default='plan.png')
    photo_3 = models.ImageField(upload_to='pics/plans', default='plan.png')
    photo_4 = models.ImageField(upload_to='pics/plans', default='plan.png')


class Week(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default=None)
    saturday_day_food_1 = models.ForeignKey(FoodDetail, related_name='saturday_day_1', on_delete=models.CASCADE,
                                            default=None)
    saturday_day_food_2 = models.ForeignKey(FoodDetail, related_name='saturday_day_2', on_delete=models.CASCADE,
                                            default=None, blank=True, null=True)
    saturday_day_food_3 = models.ForeignKey(FoodDetail, related_name='saturday_day_3', on_delete=models.CASCADE,
                                            default=None, blank=True, null=True)
    saturday_day_food_4 = models.ForeignKey(FoodDetail, related_name='saturday_day_4', on_delete=models.CASCADE,
                                            default=None, blank=True, null=True)

    saturday_night_food_1 = models.ForeignKey(FoodDetail, related_name='saturday_night_1', on_delete=models.CASCADE,
                                              default=None)
    saturday_night_food_2 = models.ForeignKey(FoodDetail, related_name='saturday_night_2', on_delete=models.CASCADE,
                                              default=None, blank=True, null=True)
    saturday_night_food_3 = models.ForeignKey(FoodDetail, related_name='saturday_night_3', on_delete=models.CASCADE,
                                              default=None, blank=True, null=True)
    saturday_night_food_4 = models.ForeignKey(FoodDetail, related_name='saturday_night_4', on_delete=models.CASCADE,
                                              default=None, blank=True, null=True)

    sunday_day_food_1 = models.ForeignKey(FoodDetail, related_name='sunday_day_1', on_delete=models.CASCADE,
                                          default=None)
    sunday_day_food_2 = models.ForeignKey(FoodDetail, related_name='sunday_day_2', on_delete=models.CASCADE,
                                          default=None, blank=True, null=True)
    sunday_day_food_3 = models.ForeignKey(FoodDetail, related_name='sunday_day_3', on_delete=models.CASCADE,
                                          default=None, blank=True, null=True)
    sunday_day_food_4 = models.ForeignKey(FoodDetail, related_name='sunday_day_4', on_delete=models.CASCADE,
                                          default=None, blank=True, null=True)

    sunday_night_food_1 = models.ForeignKey(FoodDetail, related_name='sunday_night_1', on_delete=models.CASCADE,
                                            default=None)
    sunday_night_food_2 = models.ForeignKey(FoodDetail, related_name='sunday_night_2', on_delete=models.CASCADE,
                                            default=None, blank=True, null=True)
    sunday_night_food_3 = models.ForeignKey(FoodDetail, related_name='sunday_night_3', on_delete=models.CASCADE,
                                            default=None, blank=True, null=True)
    sunday_night_food_4 = models.ForeignKey(FoodDetail, related_name='sunday_night_4', on_delete=models.CASCADE,
                                            default=None, blank=True, null=True)
    monday_day_food_1 = models.ForeignKey(FoodDetail, related_name='monday_day_1', on_delete=models.CASCADE,
                                          default=None)
    monday_day_food_2 = models.ForeignKey(FoodDetail, related_name='monday_day_2', on_delete=models.CASCADE,
                                          default=None, blank=True, null=True)
    monday_day_food_3 = models.ForeignKey(FoodDetail, related_name='monday_day_3', on_delete=models.CASCADE,
                                          default=None, blank=True, null=True)
    monday_day_food_4 = models.ForeignKey(FoodDetail, related_name='monday_day_4', on_delete=models.CASCADE,
                                          default=None, blank=True, null=True)

    monday_night_food_1 = models.ForeignKey(FoodDetail, related_name='monday_night_1', on_delete=models.CASCADE,
                                            default=None)
    monday_night_food_2 = models.ForeignKey(FoodDetail, related_name='monday_night_2', on_delete=models.CASCADE,
                                            default=None, blank=True, null=True)
    monday_night_food_3 = models.ForeignKey(FoodDetail, related_name='monday_night_3', on_delete=models.CASCADE,
                                            default=None, blank=True, null=True)
    monday_night_food_4 = models.ForeignKey(FoodDetail, related_name='monday_night_4', on_delete=models.CASCADE,
                                            default=None, blank=True, null=True)
    tuesday_day_food_1 = models.ForeignKey(FoodDetail, related_name='tuesday_day_1', on_delete=models.CASCADE,
                                           default=None)
    tuesday_day_food_2 = models.ForeignKey(FoodDetail, related_name='tuesday_day_2', on_delete=models.CASCADE,
                                           default=None, blank=True, null=True)
    tuesday_day_food_3 = models.ForeignKey(FoodDetail, related_name='tuesday_day_3', on_delete=models.CASCADE,
                                           default=None, blank=True, null=True)
    tuesday_day_food_4 = models.ForeignKey(FoodDetail, related_name='tuesday_day_4', on_delete=models.CASCADE,
                                           default=None, blank=True, null=True)

    tuesday_night_food_1 = models.ForeignKey(FoodDetail, related_name='tuesday_night_1', on_delete=models.CASCADE,
                                             default=None)
    tuesday_night_food_2 = models.ForeignKey(FoodDetail, related_name='tuesday_night_2', on_delete=models.CASCADE,
                                             default=None, blank=True, null=True)
    tuesday_night_food_3 = models.ForeignKey(FoodDetail, related_name='tuesday_night_3', on_delete=models.CASCADE,
                                             default=None, blank=True, null=True)
    tuesday_night_food_4 = models.ForeignKey(FoodDetail, related_name='tuesday_night_4', on_delete=models.CASCADE,
                                             default=None, blank=True, null=True)
    wednesday_day_food_1 = models.ForeignKey(FoodDetail, related_name='wednesday_day_1', on_delete=models.CASCADE,
                                             default=None)
    wednesday_day_food_2 = models.ForeignKey(FoodDetail, related_name='wednesday_day_2', on_delete=models.CASCADE,
                                             default=None, blank=True, null=True)
    wednesday_day_food_3 = models.ForeignKey(FoodDetail, related_name='wednesday_day_3', on_delete=models.CASCADE,
                                             default=None, blank=True, null=True)
    wednesday_day_food_4 = models.ForeignKey(FoodDetail, related_name='wednesday_day_4', on_delete=models.CASCADE,
                                             default=None, blank=True, null=True)

    wednesday_night_food_1 = models.ForeignKey(FoodDetail, related_name='wednesday_night_1', on_delete=models.CASCADE,
                                               default=None)
    wednesday_night_food_2 = models.ForeignKey(FoodDetail, related_name='wednesday_night_2', on_delete=models.CASCADE,
                                               default=None, blank=True, null=True)
    wednesday_night_food_3 = models.ForeignKey(FoodDetail, related_name='wednesday_night_3', on_delete=models.CASCADE,
                                               default=None, blank=True, null=True)
    wednesday_night_food_4 = models.ForeignKey(FoodDetail, related_name='wednesday_night_4', on_delete=models.CASCADE,
                                               default=None, blank=True, null=True)
    thursday_day_food_1 = models.ForeignKey(FoodDetail, related_name='thursday_day_1', on_delete=models.CASCADE,
                                            default=None)
    thursday_day_food_2 = models.ForeignKey(FoodDetail, related_name='thursday_day_2', on_delete=models.CASCADE,
                                            default=None, blank=True, null=True)
    thursday_day_food_3 = models.ForeignKey(FoodDetail, related_name='thursday_day_3', on_delete=models.CASCADE,
                                            default=None, blank=True, null=True)
    thursday_day_food_4 = models.ForeignKey(FoodDetail, related_name='thursday_day_4', on_delete=models.CASCADE,
                                            default=None, blank=True, null=True)

    thursday_night_food_1 = models.ForeignKey(FoodDetail, related_name='thursday_night_1', on_delete=models.CASCADE,
                                              default=None)
    thursday_night_food_2 = models.ForeignKey(FoodDetail, related_name='thursday_night_2', on_delete=models.CASCADE,
                                              default=None, blank=True, null=True)
    thursday_night_food_3 = models.ForeignKey(FoodDetail, related_name='thursday_night_3', on_delete=models.CASCADE,
                                              default=None, blank=True, null=True)
    thursday_night_food_4 = models.ForeignKey(FoodDetail, related_name='thursday_night_4', on_delete=models.CASCADE,
                                              default=None, blank=True, null=True)
    friday_day_food_1 = models.ForeignKey(FoodDetail, related_name='friday_day_1', on_delete=models.CASCADE,
                                          default=None)
    friday_day_food_2 = models.ForeignKey(FoodDetail, related_name='friday_day_2', on_delete=models.CASCADE,
                                          default=None, blank=True, null=True)
    friday_day_food_3 = models.ForeignKey(FoodDetail, related_name='friday_day_3', on_delete=models.CASCADE,
                                          default=None, blank=True, null=True)
    friday_day_food_4 = models.ForeignKey(FoodDetail, related_name='friday_day_4', on_delete=models.CASCADE,
                                          default=None, blank=True, null=True)

    friday_night_food_1 = models.ForeignKey(FoodDetail, related_name='friday_night_1', on_delete=models.CASCADE,
                                            default=None)
    friday_night_food_2 = models.ForeignKey(FoodDetail, related_name='friday_night_2', on_delete=models.CASCADE,
                                            default=None, blank=True, null=True)
    friday_night_food_3 = models.ForeignKey(FoodDetail, related_name='friday_night_3', on_delete=models.CASCADE,
                                            default=None, blank=True, null=True)
    friday_night_food_4 = models.ForeignKey(FoodDetail, related_name='friday_night_4', on_delete=models.CASCADE,
                                            default=None, blank=True, null=True)
