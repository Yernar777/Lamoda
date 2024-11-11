from django.db import models

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
