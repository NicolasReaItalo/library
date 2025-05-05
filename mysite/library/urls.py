from django.urls import path
from .views import list_books

urlpatterns = [
    path("list/", list_books),
]
