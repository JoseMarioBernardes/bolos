from django.urls import path
from .views import (
    SaleListView,
    SaleDetailView,
    SaleCreateView,
    SaleUpdateView,
    SaleDeleteView,
)

urlpatterns = [
    path('', SaleListView.as_view(), name='sale_list'),
    path('novo/', SaleCreateView.as_view(), name='sale_create'),
    path('<int:pk>/', SaleDetailView.as_view(), name='sale_detail'),
    path('<int:pk>/editar/', SaleUpdateView.as_view(), name='sale_update'),
    path('<int:pk>/excluir/', SaleDeleteView.as_view(), name='sale_delete'),
]
