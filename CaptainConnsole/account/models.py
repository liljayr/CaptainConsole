from django.db import models

# Create your models here.
from consoles.models import Consoles
from games.models import Games


class Account(models.Model):
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    favorites = models.CharField(max_length=999)
    recently_viewed = models.CharField(max_length=999)

#class Product(models.Model):
 #   game = models.ForeignKey(Games, on_delete=models.CASCADE)
  #  console = models.ForeignKey(Consoles, on_delete=models.CASCADE)
   # account = models.ForeignKey(Account, on_delete=models.CASCADE)

class Order(models.Model):
    products =models.CharField(max_length=999)
    email = models.CharField(max_length=225)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

class AccountImage(models.Model):
    image = models.CharField(max_length=999)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)