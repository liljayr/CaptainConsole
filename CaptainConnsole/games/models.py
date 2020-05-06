from django.db import models
from consoles.models import Consoles

#id column is default created as primary key, autoincrement

class GameCategory(models.Model):
    name = models.CharField(max_length=255)

class Games(models.Model):
    name = models.CharField(max_length=255)     #blank = True makes it a non required field
    description = models.CharField(max_length=999)
    category = models.ForeignKey(GameCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    onSale = models.BooleanField()
    console = models.ForeignKey(Consoles, on_delete=models.CASCADE)       #TODO: Map to console


class GameImage(models.Model):
    image = models.CharField(max_length=999)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)