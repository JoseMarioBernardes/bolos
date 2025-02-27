from django.urls import path
from .views import (
    CustomerListView,
    CustomerDetailView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
)

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('novo/', CustomerCreateView.as_view(), name='customer_create'),
    path('<int:pk>/editar/', CustomerUpdateView.as_view(), name='customer_update'),
    path('<int:pk>/excluir/', CustomerDeleteView.as_view(), name='customer_delete'),
]
