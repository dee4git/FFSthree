from django import forms

from .models import Store, Week, FoodDetail, Plan


class Form(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            "name",
            "location",
            "phone",
            "description",
            "display_picture",
        ]


class FoodForm(forms.ModelForm):
    class Meta:
        model = FoodDetail
        fields = [
            "name",
            "category",
            "amount",
            "calorie",
        ]


class WeekForm(forms.ModelForm):
    class Meta:
        model = Week
        fields = [
            'saturday_day_food_1',
            'saturday_day_food_2',
            'saturday_day_food_3',
            'saturday_day_food_4',
            'saturday_night_food_1',
            'saturday_night_food_2',
            'saturday_night_food_3',
            'saturday_night_food_4',
            'sunday_day_food_1',
            'sunday_day_food_2',
            'sunday_day_food_3',
            'sunday_day_food_4',
            'sunday_night_food_1',
            'sunday_night_food_2',
            'sunday_night_food_3',
            'sunday_night_food_4',
            'monday_day_food_1',
            'monday_day_food_2',
            'monday_day_food_3',
            'monday_day_food_4',
            'monday_night_food_1',
            'monday_night_food_2',
            'monday_night_food_3',
            'monday_night_food_4',
            'tuesday_day_food_1',
            'tuesday_day_food_2',
            'tuesday_day_food_3',
            'tuesday_day_food_4',
            'tuesday_night_food_1',
            'tuesday_night_food_2',
            'tuesday_night_food_3',
            'tuesday_night_food_4',
            'wednesday_day_food_1',
            'wednesday_day_food_2',
            'wednesday_day_food_3',
            'wednesday_day_food_4',
            'wednesday_night_food_1',
            'wednesday_night_food_2',
            'wednesday_night_food_3',
            'wednesday_night_food_4',
            'thursday_day_food_1',
            'thursday_day_food_2',
            'thursday_day_food_3',
            'thursday_day_food_4',
            'thursday_night_food_1',
            'thursday_night_food_2',
            'thursday_night_food_3',
            'thursday_night_food_4',
            'friday_day_food_1',
            'friday_day_food_2',
            'friday_day_food_3',
            'friday_day_food_4',
            'friday_night_food_1',
            'friday_night_food_2',
            'friday_night_food_3',
            'friday_night_food_4',
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(WeekForm, self).__init__(*args, **kwargs)
        """what happens here is we get all the stores under a user
         then get the foods under those store in the foods variable
         """
        foods = FoodDetail.objects.none()
        stores = Store.objects.filter(owner=self.user)
        for i in stores:
            foods |= FoodDetail.objects.filter(store=i)

        self.fields['saturday_day_food_1'].queryset = foods
        self.fields['saturday_day_food_1'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['saturday_day_food_2'].queryset = foods
        self.fields['saturday_day_food_2'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['saturday_day_food_3'].queryset = foods
        self.fields['saturday_day_food_3'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['saturday_day_food_4'].queryset = foods
        self.fields['saturday_day_food_4'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['saturday_night_food_1'].queryset = foods
        self.fields['saturday_night_food_1'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['saturday_night_food_2'].queryset = foods
        self.fields['saturday_night_food_2'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['saturday_night_food_3'].queryset = foods
        self.fields['saturday_night_food_3'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['saturday_night_food_4'].queryset = foods
        self.fields['saturday_night_food_4'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)

        self.fields['sunday_day_food_1'].queryset = foods
        self.fields['sunday_day_food_1'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['sunday_day_food_2'].queryset = foods
        self.fields['sunday_day_food_2'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['sunday_day_food_3'].queryset = foods
        self.fields['sunday_day_food_3'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['sunday_day_food_4'].queryset = foods
        self.fields['sunday_day_food_4'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['sunday_night_food_1'].queryset = foods
        self.fields['sunday_night_food_1'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['sunday_night_food_2'].queryset = foods
        self.fields['sunday_night_food_2'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['sunday_night_food_3'].queryset = foods
        self.fields['sunday_night_food_3'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['sunday_night_food_4'].queryset = foods
        self.fields['sunday_night_food_4'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)

        self.fields['monday_day_food_1'].queryset = foods
        self.fields['monday_day_food_1'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['monday_day_food_2'].queryset = foods
        self.fields['monday_day_food_2'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['monday_day_food_3'].queryset = foods
        self.fields['monday_day_food_3'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['monday_day_food_4'].queryset = foods
        self.fields['monday_day_food_4'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['monday_night_food_1'].queryset = foods
        self.fields['monday_night_food_1'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['monday_night_food_2'].queryset = foods
        self.fields['monday_night_food_2'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['monday_night_food_3'].queryset = foods
        self.fields['monday_night_food_3'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['monday_night_food_4'].queryset = foods
        self.fields['monday_night_food_4'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)

        self.fields['tuesday_day_food_1'].queryset = foods
        self.fields['tuesday_day_food_1'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['tuesday_day_food_2'].queryset = foods
        self.fields['tuesday_day_food_2'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['tuesday_day_food_3'].queryset = foods
        self.fields['tuesday_day_food_3'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['tuesday_day_food_4'].queryset = foods
        self.fields['tuesday_day_food_4'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['tuesday_night_food_1'].queryset = foods
        self.fields['tuesday_night_food_1'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['tuesday_night_food_2'].queryset = foods
        self.fields['tuesday_night_food_2'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['tuesday_night_food_3'].queryset = foods
        self.fields['tuesday_night_food_3'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['tuesday_night_food_4'].queryset = foods
        self.fields['tuesday_night_food_4'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)

        self.fields['wednesday_day_food_1'].queryset = foods
        self.fields['wednesday_day_food_1'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['wednesday_day_food_2'].queryset = foods
        self.fields['wednesday_day_food_2'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['wednesday_day_food_3'].queryset = foods
        self.fields['wednesday_day_food_3'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['wednesday_day_food_4'].queryset = foods
        self.fields['wednesday_day_food_4'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['wednesday_night_food_1'].queryset = foods
        self.fields['wednesday_night_food_1'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['wednesday_night_food_2'].queryset = foods
        self.fields['wednesday_night_food_2'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['wednesday_night_food_3'].queryset = foods
        self.fields['wednesday_night_food_3'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['wednesday_night_food_4'].queryset = foods
        self.fields['wednesday_night_food_4'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)

        self.fields['thursday_day_food_1'].queryset = foods
        self.fields['thursday_day_food_1'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['thursday_day_food_2'].queryset = foods
        self.fields['thursday_day_food_2'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['thursday_day_food_3'].queryset = foods
        self.fields['thursday_day_food_3'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['thursday_day_food_4'].queryset = foods
        self.fields['thursday_day_food_4'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['thursday_night_food_1'].queryset = foods
        self.fields['thursday_night_food_1'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['thursday_night_food_2'].queryset = foods
        self.fields['thursday_night_food_2'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['thursday_night_food_3'].queryset = foods
        self.fields['thursday_night_food_3'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['thursday_night_food_4'].queryset = foods
        self.fields['thursday_night_food_4'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)

        self.fields['friday_day_food_1'].queryset = foods
        self.fields['friday_day_food_1'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['friday_day_food_2'].queryset = foods
        self.fields['friday_day_food_2'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['friday_day_food_3'].queryset = foods
        self.fields['friday_day_food_3'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['friday_day_food_4'].queryset = foods
        self.fields['friday_day_food_4'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['friday_night_food_1'].queryset = foods
        self.fields['friday_night_food_1'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['friday_night_food_2'].queryset = foods
        self.fields['friday_night_food_2'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['friday_night_food_3'].queryset = foods
        self.fields['friday_night_food_3'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)
        self.fields['friday_night_food_4'].queryset = foods
        self.fields['friday_night_food_4'].label_from_instance = lambda obj: "%s %s " % (obj.name, obj.amount)


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = [
            'name',
            'price',
            'capacity',
            'category',
            'total_estimated_calorie',
        ]
