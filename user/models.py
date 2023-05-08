from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    postal_code = models.IntegerField()

class UserPayment(models.Model):
    user = models.ForeignKey(User)
    cvv = models.IntegerField()
    expiration_date = models.FloatField()
    number = models.IntegerField()
