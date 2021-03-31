from django.db.models import Q
from django.shortcuts import render, redirect
import datetime
from stores.models import Plan, Store
from . import forms
from .models import DeliveryFighter, FighterRequest, Meal
from enrolments.models import ExtendedUser, Enrolment
from enrolments.views import set_profile
from enrolments.models import ExtendedUser


# Create your views here.
def sent_meal(request):
    today = datetime.date.today()
    # delivery_fighter = DeliveryFighter.objects.get(user=ExtendedUser.objects.get(user=request.user))
    # store_owner = delivery_fighter.store.owner
    today_meal = Meal.objects.filter(date=today, creator=request.user)
    return render(request,'list_of_customers.html',{
        "today_meal":today_meal,
    })


def send_meal(request):
    today = datetime.date.today()
    try:
        stores = Store.objects.filter(owner=request.user)
        enrolments = Enrolment.objects.none()
        plans = Plan.objects.none()
        for i in stores:
            plans |= Plan.objects.filter(store=i)
        for i in plans:
            enrolments |= Enrolment.objects.filter(plan=i)
        # valid enrolments are those in which today is inside the start and end date and has at least 1 meal today.
        try:
            valid_enrolments = enrolments.filter(Q(start_date__lte=today),
                                                 (Q(end_date__gte=today) | Q(end_date=None)),
                                                 (Q(day_meal_count__gt=0)) | (Q(night_meal_count__gt=0))
                                                 )
            for i in valid_enrolments:
                print(i)
                Meal(creator=request.user, enrolment=i).save()
                # meal.save()
            return sent_meal(request)
        except:
            return list_of_customers(request)
    except:
        return list_of_customers(request)


def list_of_customers(request):
    today = datetime.date.today()
    try:
        stores = Store.objects.filter(owner=request.user)
        enrolments = Enrolment.objects.none()
        plans = Plan.objects.none()
        for i in stores:
            plans |= Plan.objects.filter(store=i)
        for i in plans:
            enrolments |= Enrolment.objects.filter(plan=i)
        # valid enrolments are those in which today is inside the start and end date and has at least 1 meal today.
        try:
            valid_enrolments = enrolments.filter(Q(start_date__lte=today),
                                                 (Q(end_date__gte=today) | Q(end_date=None)),
                                                 (Q(day_meal_count__gt=0)) | (Q(night_meal_count__gt=0))
                                                 )
            return render(request, 'list_of_customers.html',
                          {
                              "valid_enrolments": valid_enrolments,
                          }
                          )
        except:
            return render(request, 'list_of_customers.html')

    except:
        return render(request, 'list_of_customers.html')


def all_fighters(request):
    fighters = DeliveryFighter.objects.all()
    try:
        requested = FighterRequest.objects.filter(requester=request.user)
        for i in requested:
            fighters = fighters.exclude(pk=i.fighter.pk)
        return render(request, 'all_fighters.html', {
            "fighters": fighters,
            "requested": requested,
        })
    except:
        return render(request, 'all_fighters.html', {
            "fighters": fighters,
        })


def cancel_request_fighter(request, requested_id):
    try:
        FighterRequest.objects.get(pk=requested_id).delete()
        return all_fighters(request)
    except:
        return all_fighters(request)


def accept_store_request(request, requested_id):
    instance = FighterRequest.objects.get(pk=requested_id)
    fighter = instance.fighter
    store = instance.store_request
    fighter.store = store
    fighter.save()
    return see_del_profile(request)


def manage_store_request(request):
    store_requests = FighterRequest.objects.filter(
        fighter=DeliveryFighter.objects.get(user=ExtendedUser.objects.get(user=request.user)))
    return render(request, 'store_request.html', {
        "store_requests": store_requests,
    })


def request_fighter(request, fighter_id):
    fighter = DeliveryFighter.objects.get(pk=fighter_id)
    if request.method == "POST":
        form = forms.FighterRequestForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.fighter = fighter
            instance.requester = request.user
            instance.save()
            return all_fighters(request)
    else:

        form = forms.FighterRequestForm(user=request.user)
    return render(request, 'fighter_request.html',
                  {"form": form,
                   }
                  )


def set_del_profile(request):
    try:
        extended_user = ExtendedUser.objects.get(user=request.user)
        if request.method == "POST":
            form = forms.DeliveryFighterForm(request.POST, request.FILES)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = extended_user
                instance.save()
                return see_del_profile(request)
        else:
            form = forms.DeliveryFighterForm()
        return render(request, 'set_del_profile.html',
                      {"form": form,
                       }
                      )
    except:
        return set_profile(request)


def edit_del_profile(request):
    delivery_fighter = DeliveryFighter.objects.get(user=request.user)
    if delivery_fighter.user == request.user:
        if request.method == "POST":
            form = forms.DeliveryFighterForm(request.POST or None, request.FILES, instance=delivery_fighter)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return see_del_profile(request)
        else:
            form = forms.DeliveryFighterForm()
        return render(request, 'set_del_profile.html',
                      {"form": form,
                       }
                      )


def see_del_profile(request):
    delivery_fighter = DeliveryFighter.objects.get(user=ExtendedUser.objects.get(user=request.user))
    today = datetime.date.today()
    try:
        store = delivery_fighter.store
        enrolments = Enrolment.objects.none()
        plans = Plan.objects.filter(store=store)
        for i in plans:
            enrolments |= Enrolment.objects.filter(plan=i)
        # valid enrolments are those in which today is inside the start and end date and has at least 1 meal today.
        try:
            valid_enrolments = enrolments.filter(Q(start_date__lte=today),
                                                 (Q(end_date__gte=today) | Q(end_date=None)),
                                                 (Q(day_meal_count__gt=0)) | (Q(night_meal_count__gt=0))
                                                 )
            return render(request, 'see_del_profile.html',
                          {
                              "delivery_fighter": delivery_fighter,
                              "store": store,
                              "valid_enrolments": valid_enrolments,
                          }
                          )
        except:
            return render(request, 'see_del_profile.html',
                          {
                              "delivery_fighter": delivery_fighter,
                              "store": store,
                          }
                          )

    except:
        return render(request, 'see_del_profile.html',
                      {
                          "delivery_fighter": delivery_fighter,
                      }
                      )
