from django.db import models
from ghost.models import Pizza
from manufacturer.models import Offer
from django.contrib.auth.models import User


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField()

class CartItems(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, blank=True, null=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, blank=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)