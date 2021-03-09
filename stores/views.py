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


def get_rating(request, store_id):
    try:
        rating_list = []
        ratings = StoreRating.objects.filter(store=Store.objects.get(pk=store_id))
        for i in ratings:
            rating_list.append(i.rating)
        return [round(mean(rating_list), 2), ratings, len(rating_list)]
    except:
        return [0, None, 0]


def view_store(request, store_id):
    status = 0  # checks if the current user is the owner
    rated = 0  # checks if the user has already rated the store
    store = Store.objects.get(pk=store_id)
    current_rating = get_rating(request, store_id)
    rating = current_rating[0]  # zeroth element contain the avg rating of the shop
    people = current_rating[2]  # number of people rated
    if store.owner == request.user:
        status = 1
    try:
        if StoreRating.objects.get(store=store_id, user=request.user):
            rated = 1
            current_rating = StoreRating.objects.get(store=store_id, user=request.user)
            return render(request, "detail_store.html", {"store": store,
                                                         "status": status,
                                                         "rated": rated,
                                                         "rating": rating,
                                                         "people": people,
                                                         "current_rating": current_rating,
                                                         # "products": products,
                                                         })
    except:
        return render(request, "detail_store.html", {"store": store,
                                                     "status": status,
                                                     "rated": rated,
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
    # rating machine begins
    reviews = get_rating(request, store_id)
    reviews = reviews[1]
    if store.owner == request.user:
        status = 1
    try:
        if StoreRating.objects.get(store=store_id, user=request.user):
            rated = 1
            current_rating = StoreRating.objects.get(store=store_id, user=request.user)
            return render(request, "comments_store.html", {"store": store,
                                                           "status": status,
                                                           "rated": rated,
                                                           "rating": rating,
                                                           "reviews": reviews,
                                                           "people": people,
                                                           "current_rating": current_rating,
                                                           # "products": products,
                                                           })
    except:
        return render(request, "comments_store.html", {"store": store,
                                                       "status": status,
                                                       "rated": rated,
                                                       "reviews": reviews
                                                       # "products": products,
                                                       })
