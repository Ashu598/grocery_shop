from django.db import models
from django.contrib.auth.models import User
from store.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=120)
    address = models.TextField()
    city = models.CharField(max_length=80)
    pincode = models.CharField(max_length=10)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_line_total(self):
        return self.price * self.quantity
