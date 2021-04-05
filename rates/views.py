from statistics import mean

from django.shortcuts import render, redirect
from delivery_fighters.models import Meal
from enrolments.models import ExtendedUser, Enrolment
from . import forms
from stores.models import Store, Plan, Week
from stores.views import view_store, view_plan, get_full_star
from django.contrib.auth.decorators import login_required
import datetime
from .models import StoreRating, MealRating


def get_meal_rating(meal_ratings):
    try:
        rating_list = []
        for i in meal_ratings:
            rating_list.append(i.rating)
        rating = round(mean(rating_list), 2)
        stars = get_full_star(rating)
        return [rating, len(rating_list), stars]
    except:
        return [0, 0, 0]


def view_plan_rating(request, plan_id):
    rated = 0  # checks if the user has already rated the store
    enrolled = 0  # checks if the user has already enrolled to the plan
    enrolment_id = 0
    plan = Plan.objects.get(pk=plan_id)
    week = Week.objects.get(plan=plan)
    extended_user = ExtendedUser.objects.get(user=request.user)
    enrolments = Enrolment.objects.filter(user=extended_user)
    for i in enrolments:
        if i.plan == plan:
            enrolled = 1
            enrolment_id = i.id

    # getting meal ratings
    meal_ratings = MealRating.objects.filter(meal__enrolment__plan=plan)
    ratings_details = get_meal_rating(meal_ratings)
    avg_rating = ratings_details[0]
    number_of_rating = ratings_details[1]
    stars = ratings_details[2]
    return render(request, 'plan_rating.html', {
        "rated": rated,
        "week": week,
        "enrolled": enrolled,
        "enrolment_id": enrolment_id,
        "meal_ratings": meal_ratings,
        "plan": plan,
        "avg_rating": avg_rating,
        "number_of_rating": number_of_rating,
        "stars": stars,
    })


def rate_meal(request, meal_id):
    meal = Meal.objects.get(pk=meal_id)
    enroller = ExtendedUser.objects.get(user=request.user)

    if request.method == "POST":
        form = forms.MealRatingForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.meal = meal
            instance.enroller = enroller
            meal.is_rated = True
            meal.save()
            instance.save()
            return view_plan(request, plan_id=meal.enrolment.plan.id)
    else:
        form = forms.MealRatingForm()

    return render(request, 'rate_meal.html', {
        "form": form,
        "meal": meal,
        # "already_rated": already_rated_meal,
    })


def edit_store_rating(request, store_id):
    current = StoreRating.objects.get(store=Store.objects.get(pk=store_id), user=request.user)
    top = "Edit your rating for " + current.store.name
    confirm = "Confirm"
    confirm_msg = "Update rating?"
    cancel = "Cancel"
    if request.method == "POST":
        form = forms.Form(request.POST or None, request.FILES, instance=current)
        if form.is_valid():
            print('is valid')
            form.save()
            return view_store(request, store_id)

    else:
        form = forms.Form(instance=current)
    return render(request, 'create.html',
                  {"form": form,
                   "top": top,
                   "cancel": cancel,
                   "confirm": confirm,
                   "confirm_msg": confirm_msg,
                   },
                  )


def already_rated(request, store_id):
    """Handles an important exception,
     when a user is trying to be redirected to rating page after logging in
     this function stops the user from rating twice
     by showing the store instead of letting the user rate again."""

    # need this try catch in case there is no rating already
    try:
        if StoreRating.objects.get(store=store_id, user=request.user):
            return True
        else:
            return False
    except:
        return False


@login_required()
def rate_store(request, store_id):
    rated = already_rated(request, store_id)
    if not rated:
        top = "Rate This Store "
        confirm = "Confirm"
        cancel = "Cancel"
        store = Store.objects.get(pk=int(store_id))
        if request.method == "POST":
            form = forms.Form(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.store = Store.objects.get(pk=int(store_id))
                instance.user = request.user
                instance.save()
                return view_store(request, store_id)
        else:
            form = forms.Form()
            form.phone = Store.objects.get(pk=int(store_id))

        return render(request, 'rate_store.html', {"form": form,
                                                   "store": store,
                                                   "top": top,
                                                   "confirm": confirm,
                                                   "cancel": cancel,
                                                   "store_id": store_id})
    else:
        return view_store(request, store_id)
