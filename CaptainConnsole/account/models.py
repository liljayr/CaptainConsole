from django.db import models
from django.contrib.auth.models import User
from consoles.models import Consoles
from games.models import Games


class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    street_name = models.CharField(max_length=225, blank=True)
    house_nr = models.FloatField(blank=True)
    city = models.CharField(max_length=225, blank=True)
    country = models.CharField(max_length=225, blank=True)
    postal_code = models.FloatField(blank=True)

class Favorite(models.Model):
    user_id = models.FloatField()
    game_id = models.FloatField()
    console_id = models.FloatField()

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Games, on_delete=models.CASCADE, blank=True)
    console_id = models.ForeignKey(Consoles, on_delete=models.CASCADE, blank=True)
    ordered = models.BooleanField()
    amount = models.FloatField() #TODO: default value 1
    order_nr = models.FloatField()

class ProfileImage(models.Model):
    image = models.CharField(max_length=999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class SearchHistory(models.Model):
    user = models.FloatField(default=0)
    category = models.CharField(max_length=255, blank=True)
    value = models.CharField(max_length=255, blank=True)