from django.shortcuts import render, redirect
from . import forms
from .models import Store
from products.models import Product
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)


def storeCreate(request):
    print("Called")
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


def storeUpdate(request, id):
    top = "Edit your store"
    confirm = "Confirm"
    confirmation = "Update Store?"
    cancel = "Cancel"
    up = Store.objects.get(pk=id)
    if request.method== "POST":
        form = forms.Form(request.POST or None, request.FILES, instance=up)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form=forms.Form(instance=up)
    return render(request, 'create.html',
                  {"form": form,
                   "top": top,
                   "cancel": cancel,
                   "confirm": confirm,
                   "confmsg": confirmation,
                   },
                  )

def storeView(request, id):
    status = 0
    detail = Store.objects.get(pk=id)
    products=Product.objects.filter(store=detail)
    if detail.owner == request.user:
        status = 1

    return render(request, "detail.html", {"store": detail,
                                           "s": status,
                                           "products": products,
                                           })


def storeDelete(request, id):
    Store.objects.get(pk=id).delete()
    return render("/")
