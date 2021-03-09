

from django.urls import path, include
from . import views
urlpatterns = [
    path('create', views.create_store, name="create_store"),
    path('stores', views.all_stores, name="all_stores"),
    path('view/<int:id>/', views.view_store, name="view_store"),
    path('update/<int:id>/', views.update_store, name="update_store"),
    path('delete/<int:id>/', views.delete_store, name="delete_Store"),
    

]
