from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, related_name="authors")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Inventory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.book} {'available' if self.available else 'not available'}"


class Loan(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Customer, on_delete=models.CASCADE)
    borrowed_at = models.DateField(auto_now_add=True)
    returned_at = models.DateField(null=True, blank=True)
