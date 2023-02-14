from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100,default='')
    position = models.CharField(max_length=40, default='')
    years = models.IntegerField()