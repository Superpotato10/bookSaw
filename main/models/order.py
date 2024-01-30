from django.contrib.auth import get_user_model
from django.db import models

from main.models import Book

User = get_user_model()


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} | {self.first_name} {self.last_name}"

    def get_order_price(self):
        return sum([item.get_total_price() for item in self.orderitem_set.all()], 0)


class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.id} - {self.product}'

    def get_total_price(self):
        return self.price * self.count
