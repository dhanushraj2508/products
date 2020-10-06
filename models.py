from django.db import models

class product(models.Model):
    productcompany = models.CharField(max_length=100)
    productname = models.CharField(max_length=100)
    productprice = models.IntegerField()
