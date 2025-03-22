from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView
from .models import Inventory
from .serializers import InventorySerializer

class InventoryListAPIView(ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

def inventory_list(request):
    inventories = Inventory.objects.all()
    return render(request, 'inventory_list.html', {'inventories': inventories})

def inventory_detail(request, id):
    inventory = get_object_or_404(Inventory, id=id)
    return render(request, 'inventory_detail.html', {'inventory': inventory})