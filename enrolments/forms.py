from django import forms

from .models import ExtendedUser


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