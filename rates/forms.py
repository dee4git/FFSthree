from django import forms

from .models import StoreRating


class Form(forms.ModelForm):
    class Meta:
        model = StoreRating
        fields = [
            'rating',
            'comment'
        ]
