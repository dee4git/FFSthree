from math import floor
from statistics import mean

from django.shortcuts import render, redirect

from rates.models import StoreRating
from . import forms
from .models import Store
# from products.models import Product
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)


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
                   "confmsg": confirmation,
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
            your_rating = StoreRating.objects.get(store=store_id, user=request.user)
            your_stars = get_full_star(your_rating.rating-1)
            return render(request, "detail_store.html", {"store": store,
                                                         "status": status,
                                                         "rated": rated,
                                                         "rating": rating,
                                                         "people": people,
                                                         "your_rating": your_stars,
                                                         "stars": stars,
                                                         # "products": products,
                                                         })
    except:
        return render(request, "detail_store.html", {"store": store,
                                                     "status": status,
                                                     "rated": rated,
                                                     "rating": rating,
                                                     "people": people,
                                                     "stars": stars,
                                                     # "products": products,
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
    reviews = get_rating(request, store_id)
    reviews = reviews[1]  # 2nd element has all the ratings of a store
    if store.owner == request.user:
        status = 1
    try:
        # enters is the user has rated the store already
        if StoreRating.objects.get(store=store_id, user=request.user):
            rated = 1
            your_rating = StoreRating.objects.get(store=store_id, user=request.user)
            your_stars = get_full_star(your_rating.rating - 1)
            return render(request, "comments_store.html", {"store": store,
                                                         "status": status,
                                                         "rated": rated,
                                                         "rating": rating,
                                                         "people": people,
                                                         "stars": stars,
                                                         "your_rating": your_stars,
                                                         "reviews": reviews
                                                         # "products": products,
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
                                                       # "products": products,
                                                       })
