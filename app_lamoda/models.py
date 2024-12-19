from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=15)
    img = models.ImageField(upload_to= 'upload',blank=True,null=True)
    def __str__(self):
        return self.name

class LamodaCategory(models.Model):
    name = models.CharField(max_length=15)
    descriptions = models.TextField()
    img = models.ImageField(upload_to= 'upload',blank=True,null=True)
    price = models.IntegerField()
    old_price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)


class LamodaShapka(models.Model):
    name = models.CharField(max_length=50)
    descriptions = models.TextField()
    img = models.ImageField(upload_to= 'upload',blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)


class LamodaShapka1(models.Model):
    name = models.CharField(max_length=50)
    descriptions = models.TextField()
    img = models.ImageField(upload_to= 'upload',blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    


class Review1(models.Model):
    email = models.EmailField()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(LamodaCategory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.quantity * self.product.price
