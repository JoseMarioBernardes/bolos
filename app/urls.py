# cakecommerce/urls.py
from django.contrib import admin
from django.urls import path, include
from views import MenuView

urlpatterns = [
    path('', MenuView.as_view(), name='home'),  # Página de menu
    path('admin/', admin.site.urls),
    path('clientes/', include('customers.urls')),
    path('bolos/', include('cakes.urls')),
    path('vendas/', include('sales.urls')),
]
    # Futuramente: path('estoque/', include('inventory.urls')),
