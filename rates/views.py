from django.shortcuts import render, redirect
from . import forms
# Create your views here.
from stores.models import Store
from stores.views import view_store
from django.contrib.auth.decorators import login_required

from .models import StoreRating


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
    if StoreRating.objects.get(store=store_id, user=request.user):
        return True
    else:
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
        return view_store(request,store_id)