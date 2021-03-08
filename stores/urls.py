

from django.urls import path, include
from . import views
urlpatterns = [
    path('create', views.storeCreate, name="createStore"),
    path('view/<int:id>/', views.storeView, name="viewStore"),
    path('update/<int:id>/', views.storeUpdate, name="updateStore"),
    path('delete/<int:id>/', views.storeDelete, name="deleteStore"),
    

]
