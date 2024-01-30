from datetime import timedelta

from django.db import models
from django.utils.timezone import now

from .author import Author
from .genre import Genre


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    image = models.ImageField(upload_to='book_covers')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name

    def is_discounted(self):
        return self.discount != 0

    def get_price(self):
        return self.price - self.discount

    def is_new(self):
        month_after_created_date = self.created_at + timedelta(days=30)
        return self.created_at < now() < month_after_created_date
