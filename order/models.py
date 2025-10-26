from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.product.price * self.product_quantity

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
