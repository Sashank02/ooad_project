from unicodedata import category
from django.db import models
# Create your models here.
class CategoriesList(models.Model):
    # id = models.AutoField(primary_key=True)
    category_name = models.TextField(primary_key=True)
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True)
    categorylist =  models.ForeignKey(CategoriesList,on_delete=models.CASCADE,null=True)
    subscription_cost = models.IntegerField(null=True)
    book_image = models.ImageField(upload_to='book_images', blank=True,null=True)

