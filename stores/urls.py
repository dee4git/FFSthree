

from django.urls import path, include
from . import views
urlpatterns = [
    path('create', views.create_store, name="create_store"),
    path('stores', views.all_stores, name="all_stores"),
    path('view/<int:store_id>/', views.view_store, name="view_store"),
    path('update/<int:store_id>/', views.update_store, name="update_store"),
    path('delete/<int:store_id>/', views.delete_store, name="delete_Store"),
    path('reviews/<int:store_id>/', views.store_review, name="store_review"),
    path('plan/add_week/<int:plan_id>>', views.add_week, name="add_week"),
    path('add_plan/<int:store_id>/', views.add_plan, name="add_plan"),
    path('manage_plans/<int:store_id>/', views.manage_plans, name="manage_plans"),
    path('add_food/<int:store_id>/', views.add_food, name="add_food"),
    path('manage_food/<int:store_id>/', views.manage_food, name="manage_food"),
    path('delete_food/<int:food_id>/', views.delete_food, name="delete_food"),


]
