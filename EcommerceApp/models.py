from django.db import models

# Create your models here.
class Registereduser(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    phnnum = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
