from django.contrib.auth.models import User
from django.db import models

from shop.models import Product


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    total_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user} | {self.product}"
