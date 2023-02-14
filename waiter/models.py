from django.db import models

# Create your models here.
class Waiter(models.Model):
    name = models.CharField(max_length=100,default='')
    last_name = models.CharField(max_length=100, default='')
    dni = models.IntegerField()