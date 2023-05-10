from django.db import models
from ingredient.models import Ingredient


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=9999)
    price = models.FloatField()
    category = models.CharField(max_length=255)
    image = models.CharField(max_length=9999)


class PizzaIngredient(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)



