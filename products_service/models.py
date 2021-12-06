from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    location = models.TextField()
    material = models.CharField(max_length=100)
    timesofuse = models.PositiveIntegerField()
    brand = models.TextField()
    slogan = models.TextField()
    recycling = models.CharField(max_length=100)
    weight = models.FloatField()
