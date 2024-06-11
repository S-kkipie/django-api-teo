from django.db import models


class Plate(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    price = models.FloatField()
