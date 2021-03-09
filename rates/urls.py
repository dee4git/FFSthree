from django.urls import path
from . import views
urlpatterns = [
    path('rate_store/<int:store_id>/', views.rate_store, name="rate_store"),
    path('edit_store/<int:store_id>/', views.edit_store_rating, name="edit_store_rating"),
]
