from django.shortcuts import render, get_object_or_404
from . models import Store
from books.views import Book

# Create your views here.
def home(request):
    books = Book.objects
    return render(request, 'home.html', {'books':books})

def bookdetail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/bookdetail.html', {'book':book})
