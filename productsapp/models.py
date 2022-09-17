from django.db import models

# Create your models here.
class Order(models.Model):
    username = models.CharField(max_length=100)
    mail = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    
    address = models.CharField(max_length=100)
    quantity = models.IntegerField()
