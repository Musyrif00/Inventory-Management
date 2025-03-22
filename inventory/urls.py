from django.urls import path
from .views import inventory_list, inventory_detail

urlpatterns = [
    path('inventory/', inventory_list, name='inventory-list'),
    path('inventory/<int:id>/', inventory_detail, name='inventory-detail'),
]
