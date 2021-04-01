from django import forms

from stores.models import Store
from .models import DeliveryFighter, FighterRequest, Meal


class CodeCollectionForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = [
            'code'
        ]


class DeliveryFighterForm(forms.ModelForm):
    class Meta:
        model = DeliveryFighter
        fields = [

        ]


class FighterRequestForm(forms.ModelForm):
    class Meta:
        model = FighterRequest
        fields = [
            'store_request',
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(FighterRequestForm, self).__init__(*args, **kwargs)
        stores = Store.objects.filter(owner=self.user)
        print(stores)
        self.fields['store_request'].queryset = stores
        self.fields['store_request'].label_from_instance = lambda obj: "%s  || Location: %s " % (obj.name, obj.location)
