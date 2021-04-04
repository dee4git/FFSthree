from django.urls import path
from . import views
urlpatterns = [
    path('rate_store/<int:store_id>/', views.rate_store, name="rate_store"),
    path('edit_store/<int:store_id>/', views.edit_store_rating, name="edit_store_rating"),
    path('rate_meal/<int:meal_id>/', views.rate_meal, name="rate_meal"),
    path('plan_ratings/<int:plan_id>/', views.view_plan_rating, name="plan_ratings"),
]
