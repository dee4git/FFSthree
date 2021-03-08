from django import forms

from .models import Store


class Form(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
           "name",
           "location",
           "dp",
        ]


