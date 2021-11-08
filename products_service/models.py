from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=20)
    location = models.TextField()
    material = models.CharField(max_length=100)
    timesofuse = models.CharField(max_length=100)
    brand = models.TextField()
    slogan = models.TextField()
    recycling = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
