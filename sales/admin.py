from django.contrib import admin
from .models import Sale

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'cake', 'customer', 'taxa_entrega', 'pago']
