from django.urls import path
from . import views
urlpatterns = [
    path('set_profile', views.set_del_profile, name="set_del_profile"),
    path('see_profile', views.see_del_profile, name="see_del_profile"),
    path('edit_profile', views.edit_del_profile, name="edit_del_profile"),
    path('all_fighters', views.all_fighters, name="all_fighters"),
    path('request_fighter/<int:fighter_id>/', views.request_fighter, name="request_fighter"),
    path('cancel_request_fighter/<int:requested_id>/', views.cancel_request_fighter, name="cancel_request_fighter"),
    path('manage_request_fighter/', views.manage_store_request, name="manage_request_fighter"),
    path('accept_store_request/<int:requested_id>/', views.accept_store_request, name="accept_store_request"),
    path('list_of_customers/', views.list_of_customers, name="list_of_customers"),
    path('send_meal/', views.send_meal, name="send_meal"),
    path('sent_meal/', views.sent_meal, name="sent_meal"),
    path('collect_code/<int:meal_id>/', views.collect_code, name="collect_code"),

]