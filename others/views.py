import math

from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from FFSthree.views import home
from enrolments.models import ExtendedUser
from enrolments.views import set_profile
from stores.models import Plan, Store, Week
from django.db.models import CharField


def search(request):
    x_plans = []
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
    plans = Plan.objects.filter()


def all_stores_sorts(request):
    pass


def all_search_sorts(request):
    pass


def ai_plan(request):
    try:
        extended_user = ExtendedUser.objects.get(user=request.user)
        bmi = extended_user.bmi
        if bmi > 25:
            message = "You are currently overweight, we recommend you to choose meals that will help you to lose " \
                      "weight. "
            return render(request, 'cooking_ai_plan.html', {
                "message": message,
                "extended_user": extended_user
            })
        elif 18 >= bmi > 24.9:
            message = "You currently have healthy weight, we recommend you to choose meals that will help you to " \
                      "maintain weight "
            return render(request, 'cooking_ai_plan.html', {
                "message": message,
                "extended_user": extended_user
            })
        else:
            message = "You are currently underweight, we recommend you to choose meals that will help you to " \
                      "gain weight "
            return render(request, 'cooking_ai_plan.html', {
                "message": message,
                "extended_user": extended_user
            })
    except:
        return set_profile(request)


def bmr(extended_user):
    weight = extended_user.weight
    height = extended_user.height
    gender = extended_user.gender
    age = extended_user.age
    ft = math.floor(height)
    inch = height - ft
    print(ft, inch)
    ft = ft * 30.48
    inch = inch * 2.54
    height = ft + inch
    if gender == 'Male':
        return round(13.397 * weight + 4.799 * height - 5.677 * age + 88.362, 2)
    if gender == 'Female':
        return round(9.247 * weight + 3.098 * height - 4.330 * age + 447.593, 2)


def choose_ai_plan(request, key):
    extended_user = ExtendedUser.objects.get(user=request.user)
    calorie = bmr(extended_user)
    lose_calorie = calorie - 200
    gain_calorie = calorie + 200
    plans = Plan.objects.none()
    if key == 1:
        plans = Plan.objects.filter(total_estimated_calorie__lt=lose_calorie)
    if key == 2:
        plans = Plan.objects.filter(total_estimated_calorie__range=[lose_calorie, gain_calorie])
    if key == 3:
        plans = Plan.objects.filter(total_estimated_calorie__gt=gain_calorie)
    return render(request, 'ai_plan_results.html',
                  {
                      "plans": plans,
                      "calorie": calorie,
                  }
                  )
