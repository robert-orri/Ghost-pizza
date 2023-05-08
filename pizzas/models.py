from django.db import models
from ingredient.models import Ingredient


# Create your models here.

class PizzaIngredient(models.Model):
    pizza = models.ForeignKey(Pizza)
    topping = models.ForeignKey(Topping)


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.CharField(max_length=255)
    image = models.CharField(max_length=9999)
    price = models.FloatField()
