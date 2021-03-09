

from django.urls import path, include
from . import views
urlpatterns = [
    path('create', views.create_store, name="create_store"),
    path('stores', views.all_stores, name="all_stores"),
    path('view/<int:store_id>/', views.view_store, name="view_store"),
    path('update/<int:store_id>/', views.update_store, name="update_store"),
    path('delete/<int:store_id>/', views.delete_store, name="delete_Store"),
    path('reviews/<int:store_id>/', views.store_review, name="store_review"),


]
