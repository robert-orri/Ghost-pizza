from django.db import models
from pizzas.models import Pizza
from offer.models import Offer
from user.models import UserInfo

# Create your models here.
class CartItems(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, blank=True, null=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, blank=True, null=True)

class Cart(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    total_price = models.FloatField()
    items = models.ForeignKey(CartItems, on_delete=models.CASCADE)
