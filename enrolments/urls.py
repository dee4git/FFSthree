

from django.urls import path
from . import views
urlpatterns = [
    path('set_profile', views.set_profile, name="set_profile"),
    path('see_profile', views.see_profile, name="see_profile"),
    path('edit_profile', views.edit_profile, name="edit_profile"),

]
