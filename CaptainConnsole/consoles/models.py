from django.db import models

class ConsoleCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Consoles(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=3000)
    category = models.ForeignKey(ConsoleCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    discount = models.FloatField(default=0)
    onSale = models.BooleanField()
    amount = models.FloatField(default=0)
    def __str__(self):
        return self.name

class ConsoleImage(models.Model):
    image = models.CharField(max_length=999)
    console = models.ForeignKey(Consoles, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
