from django.db import models
from products.models import Product, Checkout
from django.conf import settings


class CartManager(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE, null=True)
    product_prices = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    actual_prices = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    add_time = models.DateTimeField(auto_now=True)
    quantity = models.CharField(max_length=20, default=0)

    def __str__(self):
        return str(self.user)