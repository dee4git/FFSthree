from django.urls import path
from . import views
urlpatterns = [
    path('set_profile', views.set_del_profile, name="set_del_profile"),
    path('see_profile', views.see_del_profile, name="see_del_profile"),
    path('edit_profile', views.edit_del_profile, name="edit_del_profile"),
    ]