from django.urls import path
from .views import (
    CakeListView,
    CakeDetailView,
    CakeCreateView,
    CakeUpdateView,
    CakeDeleteView,
)

urlpatterns = [
    path('', CakeListView.as_view(), name='cake_list'),
    path('novo/', CakeCreateView.as_view(), name='cake_create'),
    path('<int:pk>/', CakeDetailView.as_view(), name='cake_detail'),
    path('<int:pk>/editar/', CakeUpdateView.as_view(), name='cake_update'),
    path('<int:pk>/excluir/', CakeDeleteView.as_view(), name='cake_delete'),
]
