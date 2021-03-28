from django import forms

from .models import ExtendedUser, Enrolment


class UpdateMealCountForm(forms.ModelForm):
    class Meta:
        model = Enrolment
        fields = [
            "day_meal_count",
            "night_meal_count",
            "special_note",
        ]


class EnrolmentForm(forms.ModelForm):
    class Meta:
        model = Enrolment
        fields = [
            "start_date",
            "end_date",
            "special_note",
        ]


class AddMoney(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        fields = [
            "balance",
        ]


class ExtendedUserForm(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        fields = [
            "name",
            "phone",
            "location",
            "address",
            "height",
            "weight",
            "photo",
        ]
