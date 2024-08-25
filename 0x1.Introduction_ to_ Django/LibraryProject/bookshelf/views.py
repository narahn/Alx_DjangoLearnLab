from django.shortcuts import render
from .models import Book
from django.urls import path
# Create your views here.


def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()  # Fetch all book instances from the database
      context = {'book_list': books}  # Create a context dictionary with book list
      return render(request, 'books/book_list.html', context)

urlpatterns = [    
      path('books/', book_list, name='book_list'),
]
