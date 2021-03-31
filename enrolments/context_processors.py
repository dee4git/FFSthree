from stores.models import Store
from .models import ExtendedUser, Enrolment
from delivery_fighters.models import DeliveryFighter


def extras(request):
    extended_user = 0
    try:
        enrolled_user = ExtendedUser.objects.get(user=request.user)
        if enrolled_user is not None:
            extended_user = 1
    except:
        extended_user = 0
    return {"extended_user": extended_user}


def enrolment(request):
    has_enrolment = 0
    try:
        enrolled_user = ExtendedUser.objects.get(user=request.user)
        enrolments = Enrolment.objects.filter(user=enrolled_user)
        if enrolments is not None:
            has_enrolment = 1
    except:
        has_enrolment = 0
    return {"has_enrolment": has_enrolment}


def store(request):
    has_store = 0
    try:
        stores = Store.objects.filter(owner=request.user)
        if stores is not None:
            has_store = 1
    except:
        has_store = 0
    return {"has_store": has_store}


def delivery(request):
    is_deli = 0
    try:
        enrolled_user = ExtendedUser.objects.get(user=request.user)
        delivery_fighter = DeliveryFighter.objects.get(user=enrolled_user)
        if delivery_fighter is not None:
            is_deli = 1
        else:
            is_deli = 0
    except:
        is_deli = 0
    return {"is_deli": is_deli}
