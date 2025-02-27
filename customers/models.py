# customers/models.py
from django.db import models

class Customer(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    rua = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)  # Número da casa
    bairro = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome
