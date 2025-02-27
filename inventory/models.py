# inventory/models.py
from django.db import models
from cakes.models import Cake

class Ingredient(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    preco_medio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.nome

class Recipe(models.Model):
    cake = models.OneToOneField(Cake, on_delete=models.CASCADE)
    ingredientes = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    def __str__(self):
        return f"Receita do {self.cake.nome}"

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.ingredient.nome} para {self.recipe.cake.nome}"
