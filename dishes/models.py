from django.db import models

# Create your models here.
class Dishes(models.Model):
    name = models.CharField(max_length=100,default='')
    price = models.FloatField()
    provenance = models.CharField(max_length=100, default=' ')