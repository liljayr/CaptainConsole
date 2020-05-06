from django.db import models

class ConsoleCategory(models.Model):
    name = models.CharField(max_length=255)

class Consoles(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999)
    category = models.ForeignKey(ConsoleCategory, on_delete=models.CASCADE())
    price = models.FloatField()
    onSale = models.BooleanField()

class GameImage(models.Model):
    image = models.CharField(max_length=999)
    game = models.ForeignKey(Consoles, on_delete=models.CASCADE())
