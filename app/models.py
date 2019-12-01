# Create your models here.
# from django.contrib.auth import get_user_model
from django.db import models


class Product(models.Model):
    """商品"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.name


class Sale(models.Model):
    """売上情報"""
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    users = models.ForeignKey('users.User', on_delete=models.PROTECT)
    amount = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField("商品単価")
    created_at = models.DateTimeField(auto_now=True)
