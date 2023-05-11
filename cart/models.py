from django.db import models
from pizzas.models import Pizza
from manufacturer.models import Offer
from user.models import UserInfo


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    total_price = models.FloatField()

class CartItems(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, blank=True, null=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, blank=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)