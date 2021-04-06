from django.urls import path
from . import views
urlpatterns = [
    path('set_profile', views.set_profile, name="set_profile"),
    path('see_profile', views.see_profile, name="see_profile"),
    path('edit_profile', views.edit_profile, name="edit_profile"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('view_enrolments', views.view_enrolments, name="view_enrolments"),
    path('view_meals', views.view_meals, name="view_meals"),
    path('add_money', views.add_money, name="add_money"),
    path('create_enrolment/<int:plan_id>/', views.create_enrolment, name="create_enrolment"),
    path('delete_enrolment/<int:e_id>/', views.delete_enrolment, name="delete_enrolment"),
    path('update_enrolment/<int:e_id>/', views.update_enrolment, name="update_enrolment"),
    path('update_meal_count/<int:e_id>/', views.update_meal_count, name="update_meal_count"),
    path('confirm_meal/<int:e_id>/', views.confirm_meal, name="confirm_meal"),
]
