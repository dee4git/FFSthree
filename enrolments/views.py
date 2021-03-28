from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from stores.models import Plan
from . import forms
from .models import ExtendedUser, Enrolment
import math


# Create your views here.
def delete_enrolment(request, e_id):
    Enrolment.objects.get(pk=e_id).delete()
    return view_enrolments(request)


def view_enrolments(request):
    extended_user = ExtendedUser.objects.get(user=request.user)
    enrolments = Enrolment.objects.filter(user=extended_user)
    return render(request, 'view_enrolments.html',
                  {
                      "extended_user": extended_user,
                      "enrolments": enrolments,
                  }
                  )


def confirm_meal(request, e_id):
    """ this function deducts the balance of a user on successful meal receipt."""
    enrolment = Enrolment.objects.get(pk=e_id)
    total_meal = enrolment.day_meal_count + enrolment.night_meal_count
    price = enrolment.plan.price
    extended_user = ExtendedUser.objects.get(user=request.user)
    extended_user.balance -= price * total_meal
    if extended_user.balance > 0:
        extended_user.save()
        owner = enrolment.plan.store.owner
        owner = ExtendedUser.objects.get(user=owner)
        owner.balance += price * total_meal
        owner.save()
    return view_enrolments(request)


def update_meal_count(request, e_id):
    enrolment = Enrolment.objects.get(pk=e_id)
    if enrolment.user == ExtendedUser.objects.get(user=request.user):
        if request.method == "POST":
            form = forms.UpdateMealCountForm(request.POST or None, request.FILES, instance=enrolment)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return view_enrolments(request)
        else:
            form = forms.UpdateMealCountForm()
        return render(request, 'update_meal_count.html',
                      {"form": form,
                       }
                      )
    return redirect('/')


def update_enrolment(request, e_id):
    enrolment = Enrolment.objects.get(pk=e_id)
    if enrolment.user == ExtendedUser.objects.get(user=request.user):
        if request.method == "POST":
            form = forms.EnrolmentForm(request.POST or None, request.FILES, instance=enrolment)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return view_enrolments(request)
        else:
            form = forms.EnrolmentForm()
        return render(request, 'create_enrolment.html',
                      {"form": form,
                       }
                      )
    return redirect('/')


def create_enrolment(request, plan_id):
    plan = Plan.objects.get(pk=plan_id)
    try:
        extended_user = ExtendedUser.objects.get(user=request.user)
        if extended_user is not None:
            if request.method == "POST":
                form = forms.EnrolmentForm(request.POST, request.FILES)
                if form.is_valid():
                    print('form is valid')
                    instance = form.save(commit=False)
                    instance.user = extended_user
                    instance.plan = plan
                    instance.save()
                    return view_enrolments(request)
            else:
                form = forms.EnrolmentForm()
            return render(request, 'create_enrolment.html',
                          {"form": form,
                           }
                          )
    except:
        # you hav to set you profile first.
        return set_profile(request)


def count_bmi(data):
    height = data['height']
    weight = data['weight']
    ft = math.floor(height)
    inch = weight - ft
    inch = inch / 10
    height = ft * 0.3048 + inch * 0.0254
    return round(weight / (height * height), 2)


@login_required()
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


def add_money(request):
    extended_user = ExtendedUser.objects.get(user=request.user)
    if extended_user.user == request.user:
        if request.method == "POST":
            form = forms.AddMoney(request.POST or None, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance = extended_user
                data = form.cleaned_data
                instance.balance += data['balance']
                # counting total bmi and updating it
                instance.save()
                return view_enrolments(request)
        else:
            form = forms.AddMoney()
        return render(request, 'add_money.html',
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
