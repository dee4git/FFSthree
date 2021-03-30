from django import forms

from .models import DeliveryFighter


class DeliveryFighterForm(forms.ModelForm):
    class Meta:
        model = DeliveryFighter
        fields = [
            "name",
            "phone",
            "gender",
            "preferred_location",
            "photo",
        ]

