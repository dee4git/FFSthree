from django.shortcuts import render, redirect
from . import forms
from .models import ExtendedUser
import math


# Create your views here.
def count_bmi(data):
    height = data['height']
    weight = data['weight']
    ft = math.floor(height)
    inch = weight-ft
    inch = inch/10
    height = ft*0.3048 + inch*0.0254
    return round(weight / (height * height), 2)


def set_profile(request):
    if request.method == "POST":
        form = forms.ExtendedUserForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            data = form.cleaned_data
            # counting total bmi and updating it
            bmi = count_bmi(data)
            instance.bmi = bmi
            instance.save()
            return see_profile(request)
    else:
        form = forms.ExtendedUserForm()
    return render(request, 'set_profile.html',
                  {"form": form,
                   }
                  )


def edit_profile(request):
    extended_user = ExtendedUser.objects.get(user=request.user)
    if extended_user.user == request.user:
        if request.method == "POST":
            form = forms.ExtendedUserForm(request.POST or None, request.FILES, instance=extended_user)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                data = form.cleaned_data
                # counting total bmi and updating it
                bmi = count_bmi(data)
                instance.bmi = bmi
                instance.save()
                return see_profile(request)
        else:
            form = forms.ExtendedUserForm()
        return render(request, 'set_profile.html',
                      {"form": form,
                       }
                      )


def see_profile(request):
    extended_user = ExtendedUser.objects.get(user=request.user)
    return render(request, 'see_profile.html',
                  {"extended_user": extended_user,
                   }
                  )
