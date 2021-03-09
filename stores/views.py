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


def view_store(request, store_id):
    status = 0
    rated = 0
    detail = Store.objects.get(pk=store_id)
    if detail.owner == request.user:
        status = 1
    try:
        if StoreRating.objects.get(store=store_id, user=request.user):
            rated = 1
            current_rating = StoreRating.objects.get(store=store_id, user=request.user)
            return render(request, "detail_store.html", {"store": detail,
                                                     "status": status,
                                                     "rated": rated,
                                                     "current_rating": current_rating
                                                     # "products": products,
                                                     })
    except:
        return render(request, "detail_store.html", {"store": detail,
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
