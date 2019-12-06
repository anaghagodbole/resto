from django.db import models

class Restaurant(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=200)

class Items(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    nameofitem=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=5,decimal_places=2)