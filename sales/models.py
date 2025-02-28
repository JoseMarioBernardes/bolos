# sales/models.py
from django.db import models
from customers.models import Customer
from cakes.models import Cake

class Sale(models.Model):
    data = models.DateTimeField()
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    taxa_entrega = models.DecimalField(max_digits=10, decimal_places=2)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"Venda {self.id} - {self.cake.nome} para {self.customer.nome}"
