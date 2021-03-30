from django.shortcuts import render

from . import forms
from .models import DeliveryFighter


# Create your views here.
def set_del_profile(request):
    if request.method == "POST":
        form = forms.DeliveryFighterForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return see_profile(request)
    else:
        form = forms.DeliveryFighterForm()
    return render(request, 'set_del_profile.html',
                  {"form": form,
                   }
                  )


def edit_del_profile(request):
    delivery_fighter = DeliveryFighter.objects.get(user=request.user)
    if delivery_fighter.user == request.user:
        if request.method == "POST":
            form = forms.DeliveryFighterForm(request.POST or None, request.FILES, instance=delivery_fighter)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return see_profile(request)
        else:
            form = forms.DeliveryFighterForm()
        return render(request, 'set_profile.html',
                      {"form": form,
                       }
                      )


def see_profile(request):
    delivery_fighter = DeliveryFighter.objects.get(user=request.user)
    return render(request, 'see_profile.html',
                  {"delivery_fighter": delivery_fighter,
                   }
                  )
