from django.db import models
from django.contrib.auth.models import User
from consoles.models import Consoles
from games.models import Games
from django_countries.fields import CountryField


class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    country = CountryField(blank_label='(Select country)')
    city = models.CharField(max_length=225)
    street_name = models.CharField(max_length=225)
    house_nr = models.FloatField()
    postal_code = models.CharField(max_length=225)

class CardInfo(models.Model):
    card_holder = models.CharField(max_length=225)
    card_num = models.IntegerField()
    Exp_date = models.DateField()
    CVC = models.IntegerField()

class Favorite(models.Model):
    user_id = models.FloatField()
    game_id = models.FloatField()
    console_id = models.FloatField()

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderItems(models.Model):
    order = models.ForeignKey('Order', null=True, blank=True, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Games, on_delete=models.CASCADE, blank=True, null=True)
    console_id = models.ForeignKey(Consoles, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.FloatField()  # TODO: default value 1


class ProfileImage(models.Model):
    image = models.CharField(max_length=999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class SearchHistory(models.Model):
    user = models.FloatField(default=0)
    category = models.CharField(max_length=255, blank=True)
    value = models.CharField(max_length=255, blank=True)