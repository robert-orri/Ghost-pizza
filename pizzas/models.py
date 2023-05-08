from django.db import models
from ingredient.models import Ingredient
from pizzas.models import Pizza


# Create your models here.

class PizzaIngredient(models.Model):
    pizza = models.ForeignKey(Pizza)
    topping = models.ForeignKey(Ingredient)


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.CharField(max_length=255)
    image = models.CharField(max_length=9999)
    price = models.FloatField()
