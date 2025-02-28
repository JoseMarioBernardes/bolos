# cakecommerce/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('dashboard.urls'),),
    path('admin/', admin.site.urls),
    path('clientes/', include('customers.urls')),
    path('bolos/', include('cakes.urls')),
    path('vendas/', include('sales.urls')),
]
    # Futuramente: path('estoque/', include('inventory.urls')),
