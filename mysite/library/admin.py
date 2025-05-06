from django.contrib import admin
from library.models import Author, Book, Inventory, Loan

# Register your models here.
admin.site.register(Author)
admin.site.register(Loan)
admin.site.register(Book)
admin.site.register(Inventory)
