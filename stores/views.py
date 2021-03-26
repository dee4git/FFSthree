from math import floor
from statistics import mean

from django.shortcuts import render, redirect

from rates.models import StoreRating
from . import forms
from .models import Store, Plan, FoodDetail
# from plans.models import Product
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)


def update_food(request, food_id):
    food = FoodDetail.objects.get(pk=food_id)
    store = food.store
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
    print('here')
    foods=[]
    calories = []
    for i,j in data.items():
        foods.append(j)
    for i in foods:
        if i is None:
            pass
        else:
            calories.append(i.calorie)

    # print('Final calories', sum(calories))
    return round(sum(calories),2)

def add_week(request, plan_id):
    top = "Food 1 is mandatory you may leave the rest blank"
    confirm = "Confirm"
    confirmation = "Create Week?"
    cancel = "Cancel"
    plan = Plan.objects.get(pk=plan_id)

    if request.method == "POST" or "GET":
        form = forms.WeekForm(request.POST, request.FILES)
        if form.is_valid():

            instance = form.save(commit=False)
            instance.plan = plan
            plan.visibility = True
            data = form.cleaned_data

            # coounting total calories and updating it
            calories = count_calorie(data)
            plan.total_estimated_calorie = calories
            plan.visibility = True
            plan.save()
            instance.save()
            return redirect("/")
    else:
        print('not valid yet')
        form = forms.WeekForm()

    return render(request, 'create_week.html',
                  {"form": form,
                   "top": top,
                   "cancel": cancel,
                   "confirm": confirm,
                   "confirmation": confirmation,
                   "plan_id": plan_id,
                   },
                  )


def update_plan(request, plan_id):
    top = "Edit your store"
    confirm = "Confirm"
    confirmation = "Update Plan?"
    cancel = "Cancel"
    up = Plan.objects.get(pk=plan_id)
    if request.method == "POST":
        form = forms.PlanForm(request.POST or None, request.FILES, instance=up)
        if form.is_valid():
            form.save()
            return redirect('/')

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
            return redirect("/")
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
    top = "Create your store"
    confirm = "Confirm"
    confirmation = "Create Store?"
    cancel = "Cancel"
    if request.method == "POST":
        form = forms.Form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return redirect("/")
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


def update_store(request, store_id):
    top = "Edit your store"
    confirm = "Confirm"
    confirmation = "Update Store?"
    cancel = "Cancel"
    up = Store.objects.get(pk=store_id)
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


def view_plan(request, plan_id):
    status = 0  # checks if the current user is the owner
    rated = 0  # checks if the user has already rated the store
    plan = Plan.objects.get(pk=plan_id)
    # current_rating = get_rating(request, plan_id)
    # rating = current_rating[0]  # zeroth element contain the avg rating of the shop
    # people = current_rating[2]  # number of people rated
    # stars = current_rating[3]  # number of full star
    # if plan.owner == request.user:
    #     status = 1
    try:
        if PlanRating.objects.get(plan=plan_id, user=request.user):
            rated = 1
            your_review = PlanRating.objects.get(plan=plan_id, user=request.user)
            your_stars = get_full_star(your_review.rating)
            return render(request, "detail_plan.html", {"plan": plan,
                                                        "status": status,
                                                        "rated": rated,
                                                        # "rating": rating,
                                                        # "people": people,
                                                        # "your_rating": your_stars,
                                                        # "stars": stars,
                                                        })
    except:
        return render(request, "detail_plan.html", {"plan": plan,
                                                    "status": status,
                                                    "rated": rated,
                                                    # "rating": rating,
                                                    # "people": people,
                                                    # "stars": stars,
                                                    # "plans": plans,
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
