from django.urls import path
from .views import list_books, detail_book, detail_author

urlpatterns = [
    path("", list_books),
    path("books/details/<id>/", detail_book),
    path("authors/details/<id>/", detail_author),
]
