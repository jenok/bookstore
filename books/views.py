from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book

# Create your views here.
def books(request):
    return render(request, 'book.html')

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['text']:
            book = Book()
            book.text = request.POST['text']
            book.save()
            return redirect('/books/'+str(book.id))
        else:
            return render(request, 'books/create.html')
    else:
        return render(request, 'books/create.html')

@login_required(login_url="/accounts/signup")
def shelf(request):
    books = Book.objects
    return render(request, 'books/shelf.html')
