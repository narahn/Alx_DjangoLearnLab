from django.shortcuts import render
from .models import Book

def list_books(request):
  """Displays a list of all books in the database."""
  books = Book.objects.all()
  context = {'books': books}
  return render(request, 'relationship_app/list_books.html', context)

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'library_detail.html'