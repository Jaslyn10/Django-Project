from django.db import models

# Create your models here.

class Foodiee(models.Model):
    name=models.CharField(max_length=100)
    Desc = models.TextField()
    
    updated = models.DateTimeField(auto_now=True) #updates the filed valuee everytime the instance is saved(to track ur database)
    created = models.DateTimeField(auto_now_add=True)#sets the value when instance is created
    
class FoodImages(models.Model):
    name=models.CharField(max_length=100)
    category = models.TextField()
    cost = models.FloatField()
    images=models.ImageField(upload_to="foodImages/")
    updated = models.DateTimeField(auto_now=True) #updates the filed valuee everytime the instance is saved(to track ur database)
    created = models.DateTimeField(auto_now_add=True)#sets the value when instance is created
    