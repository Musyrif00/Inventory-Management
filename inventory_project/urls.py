from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('inventory.api_urls')),  #API routes
    path('', include('inventory.urls')),  #frontend views
]

