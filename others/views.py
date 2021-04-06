from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from FFSthree.views import home
from stores.models import Plan, Store, Week
from django.db.models import CharField


def search(request):
    if request.method == 'GET':  # If the form is submitted
        keyword = request.GET.get('search_box', None)
        print('k', keyword)

        plans = Plan.objects.none()
        stores = Store.objects.none()
        weeks = Week.objects.none()
        if keyword:

            plans |= Plan.objects.filter(Q(name__contains=keyword) |
                                         Q(category__contains=keyword) |
                                         Q(price__contains=keyword) |
                                         Q(total_estimated_calorie__contains=keyword)
                                         )
            stores |= Store.objects.filter(Q(name__contains=keyword) |
                                           Q(description__contains=keyword) |
                                           Q(phone__contains=keyword) |
                                           Q(location__contains=keyword)
                                           )
            weeks |= Week.objects.filter(
                Q(saturday_day_food_1__name__contains=keyword) |
                Q(saturday_day_food_2__name__contains=keyword) |
                Q(saturday_day_food_3__name__contains=keyword) |
                Q(saturday_day_food_4__name__contains=keyword) |
                Q(saturday_night_food_1__name__contains=keyword) |
                Q(saturday_night_food_2__name__contains=keyword) |
                Q(saturday_night_food_3__name__contains=keyword) |
                Q(saturday_night_food_4__name__contains=keyword) |
                Q(sunday_day_food_1__name__contains=keyword) |
                Q(sunday_day_food_2__name__contains=keyword) |
                Q(sunday_day_food_3__name__contains=keyword) |
                Q(sunday_day_food_4__name__contains=keyword) |
                Q(sunday_night_food_1__name__contains=keyword) |
                Q(sunday_night_food_2__name__contains=keyword) |
                Q(sunday_night_food_3__name__contains=keyword) |
                Q(sunday_night_food_4__name__contains=keyword) |
                Q(monday_day_food_1__name__contains=keyword) |
                Q(monday_day_food_2__name__contains=keyword) |
                Q(monday_day_food_3__name__contains=keyword) |
                Q(monday_day_food_4__name__contains=keyword) |
                Q(monday_night_food_1__name__contains=keyword) |
                Q(monday_night_food_2__name__contains=keyword) |
                Q(monday_night_food_3__name__contains=keyword) |
                Q(monday_night_food_4__name__contains=keyword) |
                Q(tuesday_day_food_1__name__contains=keyword) |
                Q(tuesday_day_food_2__name__contains=keyword) |
                Q(tuesday_day_food_3__name__contains=keyword) |
                Q(tuesday_day_food_4__name__contains=keyword) |
                Q(tuesday_night_food_1__name__contains=keyword) |
                Q(tuesday_night_food_2__name__contains=keyword) |
                Q(tuesday_night_food_3__name__contains=keyword) |
                Q(tuesday_night_food_4__name__contains=keyword) |
                Q(wednesday_day_food_1__name__contains=keyword) |
                Q(wednesday_day_food_2__name__contains=keyword) |
                Q(wednesday_day_food_3__name__contains=keyword) |
                Q(wednesday_day_food_4__name__contains=keyword) |
                Q(wednesday_night_food_1__name__contains=keyword) |
                Q(wednesday_night_food_2__name__contains=keyword) |
                Q(wednesday_night_food_3__name__contains=keyword) |
                Q(wednesday_night_food_4__name__contains=keyword) |
                Q(thursday_day_food_1__name__contains=keyword) |
                Q(thursday_day_food_2__name__contains=keyword) |
                Q(thursday_day_food_3__name__contains=keyword) |
                Q(thursday_day_food_4__name__contains=keyword) |
                Q(thursday_night_food_1__name__contains=keyword) |
                Q(thursday_night_food_2__name__contains=keyword) |
                Q(thursday_night_food_3__name__contains=keyword) |
                Q(thursday_night_food_4__name__contains=keyword) |
                Q(friday_day_food_1__name__contains=keyword) |
                Q(friday_day_food_2__name__contains=keyword) |
                Q(friday_day_food_3__name__contains=keyword) |
                Q(friday_day_food_4__name__contains=keyword) |
                Q(friday_night_food_1__name__contains=keyword) |
                Q(friday_night_food_2__name__contains=keyword) |
                Q(friday_night_food_3__name__contains=keyword) |
                Q(friday_night_food_4__name__contains=keyword)
            )
            x_plans = []
            for i in weeks:
                if i.plan not in plans:
                    x_plans.append(i.plan)
            for i in plans:
                x_plans.append(i)

    return render(request, 'search_result.html', {
        "keyword": keyword,
        "plans": x_plans,
        "stores": stores,
    })


def all_plans_sorts(request):
    pass


def all_stores_sorts(request):
    pass


def all_search_sorts(request):
    pass


def ai_plan(request):
    pass
