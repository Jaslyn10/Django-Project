from django.db import models
from django.contrib.auth.models import User

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
    
    def __str__(self)->str:
        return f"{self.name}{self.cost}{self.category}"

#wishlist and Cart
class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ManyToManyField(FoodImages)
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True,blank=True) #null=True , blank=True in case the cart is empty
    product = models.ForeignKey(FoodImages,on_delete=models.CASCADE)
    cart_count = models.IntegerField(default=1)
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

class FoodReview(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(FoodImages,on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i,str(i)) for i in range(1,6)])
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
