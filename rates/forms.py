from django import forms

from .models import StoreRating, MealRating


class Form(forms.ModelForm):
    class Meta:
        model = StoreRating
        fields = [
            'rating',
            'comment'
        ]


class MealRatingForm(forms.ModelForm):
    class Meta:
        model = MealRating
        fields = [
            'rating',
            'comment'
        ]
