from django.shortcuts import render
from .models import Inventory, Book, Author
from django.views.decorators.http import require_GET
from django.db.models import Count, Q
from django.http import HttpResponse


# Create your views here.
@require_GET
def list_books(request):
    available = request.GET.get("available", None)
    author = request.GET.get("author")
    title = request.GET.get("title")

    if available:
        if available.lower() not in ("true", "false"):
            available = None
        books = Inventory.objects.filter(available=available)
    else:
        books = Inventory.objects.all()
    print(books)
    if author:
        books = books.filter(
            Q(book__authors__first_name__icontains=author)
            | Q(book__authors__last_name__icontains=author)
        )

    if title:
        books = books.filter(book__title__icontains=title)

    grouped_books = (
        books.values("book__title", "book__id")
        .annotate(total=Count("id"), available=Count("id", filter=Q(available=True)))
        .order_by("book__title")
    )
    return render(request, "books/list_books.html", {"grouped_books": grouped_books})


# Create your views here.
@require_GET
def detail_book(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return HttpResponse("This book does not exists", content_type="text/plain")
    authors = book.authors.all()
    return render(request, "books/detail_book.html", {"book": book, "authors": authors})


@require_GET
def detail_author(request, id):
    try:
        author = Author.objects.get(id=id)
    except Author.DoesNotExist:
        return HttpResponse("This author does not exists", content_type="text/plain")
    books = author.books.all()
    return render(
        request, "authors/detail_author.html", {"author": author, "books": books}
    )
