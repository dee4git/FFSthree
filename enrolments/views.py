from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from delivery_fighters.models import Meal
from stores.models import Plan, Store, FoodDetail
from . import forms
from .models import ExtendedUser, Enrolment
import math
import datetime
from django.db.models import Q


# Create your views here.
def dashboard(request):
    stores = Store.objects.filter(owner=request.user)
    extended_user = ExtendedUser.objects.get(user=request.user)
    foods = FoodDetail.objects.none()
    plans = Plan.objects.none()
    enrolments = Enrolment.objects.none()
    today = datetime.date.today()
    for i in stores:
        foods |= FoodDetail.objects.filter(store=i)
        plans |= Plan.objects.filter(store=i)
    for i in plans:
        enrolments |= Enrolment.objects.filter(plan=i)
    # valid enrolments are those which are inside the start and end date.
    valid_enrolments = enrolments.filter(Q(start_date__lte=today),
                                         Q(user__balance__gte=200),
                                         (Q(end_date__gte=today) | Q(end_date=None)),
                                         (Q(day_meal_count__gt=0)) | (Q(night_meal_count__gt=0))
                                         )
    lunch = []
    dinner = []
    for i in valid_enrolments:
        dinner.append(i.night_meal_count)
        lunch.append(i.day_meal_count)
    lunch = sum(lunch)
    dinner = sum(dinner)
    return render(request, 'dashboard.html', {
        "stores": stores,
        "plans": plans,
        "foods": foods,
        "enrolments": enrolments,
        "extended_user": extended_user,
        "lunch": lunch,
        "dinner": dinner,
    })


def delete_enrolment(request, e_id):
    Enrolment.objects.get(pk=e_id).delete()
    return view_enrolments(request)


def view_enrolments(request):
    extended_user = ExtendedUser.objects.get(user=request.user)
    enrolments = Enrolment.objects.filter(user=extended_user)
    meals = Meal.objects.none()
    for i in enrolments:
        meals |= Meal.objects.filter(enrolment=i)
    codes = []
    for i in meals:
        codes.append(i.code)
    print(codes)
    return render(request, 'view_enrolments.html',
                  {
                      "extended_user": extended_user,
                      "enrolments": enrolments,
                      "codes": codes,
                  }
                  )


def confirm_meal(request, e_id):
    """ this function deducts the balance of a user on successful meal receipt."""
    enrolment = Enrolment.objects.get(pk=e_id)
    total_meal = enrolment.day_meal_count + enrolment.night_meal_count
    price = enrolment.plan.price
    extended_user = ExtendedUser.objects.get(user=request.user)
    extended_user.balance -= price * total_meal
    if extended_user.balance >= 0:
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
    """ counts bmi of a floating input """
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
