from django.urls import path
from . import views

urlpatterns = [
    path('notify', views.test_notification, name="notify"),
]
