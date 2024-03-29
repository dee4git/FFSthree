from math import floor
from statistics import mean
from django.shortcuts import render, redirect
from enrolments.models import ExtendedUser, Enrolment
from enrolments.views import set_profile
from rates.models import StoreRating, MealRating
from . import forms
from .models import Store, Plan, FoodDetail, Week
# from plans.models import Product
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)


def update_food(request, food_id):
    food = FoodDetail.objects.get(pk=food_id)
    store = food.store
    if store.owner == request.user:
        if request.method == "POST":
            form = forms.FoodForm(request.POST or None, request.FILES, instance=food)
            if form.is_valid():
                form.save()
                return manage_food(request, store.id)

        else:
            form = forms.FoodForm(instance=food)
        return render(request, 'add_food.html',
                      {"form": form,
                       },
                      )


def delete_food(request, food_id):
    food = FoodDetail.objects.get(pk=food_id)
    store = food.store
    food.delete()
    return manage_food(request, store.id)


def manage_food(request, store_id):
    foods = FoodDetail.objects.filter(store=Store.objects.get(pk=store_id))
    return render(request, 'all_foods.html', {
        'foods': foods,
        'store_id': store_id,
    })


def add_food(request, store_id):
    if request.method == "POST" or "GET":
        form = forms.FoodForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            store = Store.objects.get(pk=store_id)
            instance.store = store
            instance.save()
            return manage_food(request, store_id)
    else:
        form = forms.FoodForm()

    return render(request, 'add_food.html',
                  {"form": form,
                   },
                  )

def count_calorie(data):
    """This functtion counts the total calore while creating week for a plan"""
    foods=[]
    calories = []
    for i,j in data.items():
        foods.append(j)
    for i in foods:
        if i is None:
            pass
        else:
            calories.append(i.calorie)

    return round(sum(calories),2)

def add_week(request, plan_id):
    top = "Food 1 is mandatory you may leave the rest blank"
    confirm = "Confirm"
    confirmation = "Create Week?"
    cancel = "Cancel"
    plan = Plan.objects.get(pk=plan_id)
    store = plan.store
    # foods = FoodDetail.objects.filter(store=plan.store)
    if request.method == "POST" or "GET":
        form = forms.WeekForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            ch = form.cleaned_data.get('choice')
            instance = form.save(commit=False)
            instance.plan = plan
            plan.visibility = True
            data = form.cleaned_data

            # coounting total calories and updating it
            calories = count_calorie(data)
            plan.total_estimated_calorie = calories/7  # avg calorie per day
            plan.visibility = True
            plan.save()
            instance.save()
            return published_plans(request,store.id)
    else:
        form = forms.WeekForm(user=request.user)

    return render(request, 'create_week.html',
                  {"form": form,
                   "top": top,
                   "cancel": cancel,
                   "confirm": confirm,
                   "confirmation": confirmation,
                   "plan_id": plan_id,
                   "store_id": store.id,
                   },
                  )


def update_plan(request, plan_id):
    top = "Edit your store"
    confirm = "Confirm"
    confirmation = "Update Plan?"
    cancel = "Cancel"
    up = Plan.objects.get(pk=plan_id)
    store = up.store

    if up.store.owner == request.user:
        if request.method == "POST":
            form = forms.PlanForm(request.POST or None, request.FILES, instance=up)
            if form.is_valid():
                form.save()
                return published_plans(request, store.id)

        else:
            form = forms.PlanForm(instance=up)
        return render(request, 'create.html',
                      {"form": form,
                       "top": top,
                       "cancel": cancel,
                       "confirm": confirm,
                       "confmsg": confirmation,
                       },
                      )


def add_plan(request, store_id):
    top = "Create your Plan"
    confirm = "Confirm"
    confirmation = "Create Plan?"
    cancel = "Cancel"
    if request.method == "POST":
        form = forms.PlanForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.store = Store.objects.get(pk=store_id)
            instance.save()
            return manage_plans(request,store_id)
    else:
        form = forms.PlanForm()
    return render(request, 'create.html',
                  {"form": form,
                   "top": top,
                   "cancel": cancel,
                   "confirm": confirm,
                   "confirmation": confirmation,
                   },
                  )


def manage_plans(request, store_id):
    """This function handles the unpublished plans"""

    store = Store.objects.get(pk=store_id)
    plans = Plan.objects.filter(store=store, visibility=False)
    return render(request, 'manage_plans.html', {
        "store": store,
        "plans": plans,
    })


def published_plans(request, store_id):
    """This function handles the published plans"""

    store = Store.objects.get(pk=store_id)
    plans = Plan.objects.filter(store=store, visibility=True)
    return render(request, 'published_plans.html', {
        "store": store,
        "plans": plans,
    })


def create_store(request):
    """can craete store before setting up profile"""
    top = "Create your store"
    confirm = "Confirm"
    confirmation = "Create Store?"
    cancel = "Cancel"
    try:
        extended_user = ExtendedUser.objects.get(user=request.user)
        if extended_user is not None:
            # then create store
            if request.method == "POST":
                form = forms.Form(request.POST, request.FILES)
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.owner = request.user
                    instance.save()
                    return view_store(request,store_id = instance.id)
            else:
                form = forms.Form()
            return render(request, 'create.html',
                          {"form": form,
                           "top": top,
                           "cancel": cancel,
                           "confirm": confirm,
                           "confirmation": confirmation,
                           },
                          )
    except:
        return set_profile(request)


def update_store(request, store_id):
    top = "Edit your store"
    confirm = "Confirm"
    confirmation = "Update Store?"
    cancel = "Cancel"
    up = Store.objects.get(pk=store_id)
    if up.owner == request.user:
        if request.method == "POST":
            form = forms.Form(request.POST or None, request.FILES, instance=up)
            if form.is_valid():
                form.save()
                return view_store(request, store_id)

        else:
            form = forms.Form(instance=up)
        return render(request, 'create.html',
                      {"form": form,
                       "top": top,
                       "cancel": cancel,
                       "confirm": confirm,
                       "confmsg": confirmation,
                       },
                      )


def get_full_star(rating):
    stars = ''
    full_star = floor(rating)
    fraction = rating - full_star
    for i in range(full_star):
        stars += '⭐'

    return stars


def get_rating(request, store_id):
    try:
        rating_list = []
        ratings = StoreRating.objects.filter(store=Store.objects.get(pk=store_id))
        for i in ratings:
            rating_list.append(i.rating)
        rating = round(mean(rating_list), 2)
        stars = get_full_star(rating)
        return [rating, ratings, len(rating_list), stars]
    except:
        return [0, None, 0, 0]


def view_store(request, store_id):
    try:
        # will show plans if there is any
        return store_plan(request, store_id)
    except:
        # will just view the store if there is no plan
        status = 0  # checks if the current user is the owner
        rated = 0  # checks if the user has already rated the store
        store = Store.objects.get(pk=store_id)
        current_rating = get_rating(request, store_id)
        rating = current_rating[0]  # zeroth element contain the avg rating of the shop
        people = current_rating[2]  # number of people rated
        stars = current_rating[3]  # number of full star
        if store.owner == request.user:
            status = 1
        try:
            if StoreRating.objects.get(store=store_id, user=request.user):
                rated = 1
                your_review = StoreRating.objects.get(store=store_id, user=request.user)
                your_stars = get_full_star(your_review.rating)
                return render(request, "detail_store.html", {"store": store,
                                                             "status": status,
                                                             "rated": rated,
                                                             "rating": rating,
                                                             "people": people,
                                                             "your_rating": your_stars,
                                                             "stars": stars,
                                                             # "plans": plans,
                                                             })
        except:
            return render(request, "detail_store.html", {"store": store,
                                                         "status": status,
                                                         "rated": rated,
                                                         "rating": rating,
                                                         "people": people,
                                                         "stars": stars,
                                                         # "plans": plans,
                                                         })

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


def view_plan(request, plan_id):

    status = 0  # checks if the current user is the owner
    rated = 0  # checks if the user has already rated the store
    enrolled = 0 # checks if the user has alrady enrolled to the plan
    enrolment_id = 0
    plan = Plan.objects.get(pk=plan_id)
    week = Week.objects.get(plan = plan)
    try:
        extended_user = ExtendedUser.objects.get(user=request.user)
        enrolments = Enrolment.objects.filter(user=extended_user)
        for i in enrolments:
            if i.plan == plan:
                enrolled = 1
                enrolment_id = i.id
    except:
        # if the user is not logged in.
        enrolled = 0
    # getting meal ratings
    meal_ratings = MealRating.objects.filter(meal__enrolment__plan=plan)
    ratings_details = get_meal_rating(meal_ratings)
    avg_rating = ratings_details[0]
    number_of_rating = ratings_details[1]
    stars = ratings_details[2]

    return render(request, "detail_plan.html", {"plan": plan,
                                                "week": week,
                                                "status": status,
                                                "rated": rated,
                                                "enrolled": enrolled,
                                                "enrolment_id": enrolment_id,
                                                "avg_rating": avg_rating,
                                                "number_of_rating": number_of_rating,
                                                "stars": stars,
                                                })


def delete_store(request, store_id):
    Store.objects.get(pk=store_id).delete()
    return redirect("/")


def all_stores(request):
    stores = Store.objects.all()
    return render(request, 'all_stores.html', {
        'stores': stores
    })


def store_review(request, store_id):
    status = 0  # checks if the current user is the owner
    rated = 0  # checks if the user has already rated the store
    store = Store.objects.get(pk=store_id)
    current_rating = get_rating(request, store_id)
    rating = current_rating[0]  # zeroth element contain the avg rating of the shop
    people = current_rating[2]  # number of people rated
    stars = current_rating[3]  # number of full star
    # rating machine begins
    reviews = current_rating[1]  # 2nd element has all the ratings of a store
    if store.owner == request.user:
        status = 1
    try:
        # enters is the user has rated the store already
        if StoreRating.objects.get(store=store_id, user=request.user):
            rated = 1
            your_review = StoreRating.objects.get(store=store_id, user=request.user)
            your_stars = get_full_star(your_review.rating)
            return render(request, "comments_store.html", {"store": store,
                                                           "status": status,
                                                           "rated": rated,
                                                           "rating": rating,
                                                           "people": people,
                                                           "stars": stars,
                                                           "your_rating": your_stars,
                                                           "reviews": reviews
                                                           # "plans": plans,
                                                           })
    except:
        # enters is the user has not rated the store
        return render(request, "comments_store.html", {"store": store,
                                                       "status": status,
                                                       "rated": rated,
                                                       "rating": rating,
                                                       "people": people,
                                                       "stars": stars,
                                                       "reviews": reviews
                                                       # "plans": plans,
                                                       })


def store_plan(request, store_id):
    status = 0  # checks if the current user is the owner
    rated = 0  # checks if the user has already rated the store
    store = Store.objects.get(pk=store_id)
    try:
        plans = Plan.objects.filter(store = store, visibility= True)
    except:
        view_store(request,store_id)
    current_rating = get_rating(request, store_id)
    rating = current_rating[0]  # zeroth element contain the avg rating of the shop
    people = current_rating[2]  # number of people rated
    stars = current_rating[3]  # number of full star
    # rating machine begins
    reviews = current_rating[1]  # 2nd element has all the ratings of a store
    if store.owner == request.user:
        status = 1
    try:
        # enters is the user has rated the store already
        if StoreRating.objects.get(store=store_id, user=request.user):
            rated = 1
            your_review = StoreRating.objects.get(store=store_id, user=request.user)
            your_stars = get_full_star(your_review.rating)
            return render(request, "plans_store.html", {"store": store,
                                                        "status": status,
                                                        "rated": rated,
                                                        "rating": rating,
                                                        "people": people,
                                                        "stars": stars,
                                                        "your_rating": your_stars,
                                                        "reviews": reviews,
                                                        "plans": plans,
                                                        })
    except:
        # enters is the user has not rated the store
        return render(request, "plans_store.html", {"store": store,
                                                    "status": status,
                                                    "rated": rated,
                                                    "rating": rating,
                                                    "people": people,
                                                    "stars": stars,
                                                    "reviews": reviews,
                                                    "plans": plans,
                                                    })

