from django.db import models

# Create your models here.
from consoles.models import Consoles
from games.models import Games


class Accounts(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    user_name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    street_name = models.CharField(max_length=225, blank=True)
    house_nr = models.FloatField()
    city = models.CharField(max_length=225, blank=True)
    country = models.CharField(max_length=225, blank=True)
    postal_code = models.FloatField()
    password = models.CharField(max_length=225)
    role = models.CharField(max_length=225, blank=True)

class Favorites(models.Model):
    account_id = models.ForeignKey(Accounts, on_delete=models.CASCADE, default=0)
    game_id = models.ForeignKey(Games, on_delete=models.CASCADE, blank=True)
    console_id = models.ForeignKey(Consoles, on_delete=models.CASCADE, blank=True)

class Orders(models.Model):
    account_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Games, on_delete=models.CASCADE, blank=True)
    console_id = models.ForeignKey(Consoles, on_delete=models.CASCADE, blank=True)
    ordered = models.BooleanField()
    amount = models.FloatField() #TODO: default value 1
    order_nr = models.FloatField()

class AccountImage(models.Model):
    image = models.CharField(max_length=999)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)