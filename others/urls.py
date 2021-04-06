from django.urls import path
from . import views

urlpatterns = [
    path('search', views.search, name="search"),
    path('all_plans_sorts', views.all_plans_sorts, name="all_plans_sorts"),
    path('all_stores_sorts', views.all_stores_sorts, name="all_stores_sorts"),
    path('all_search_sorts', views.all_search_sorts, name="all_search_sorts"),
    path('ai_plan', views.ai_plan, name="ai_plan"),
    path('choose_ai_plan/<int:key>', views.choose_ai_plan, name="choose_ai_plan"),
]
