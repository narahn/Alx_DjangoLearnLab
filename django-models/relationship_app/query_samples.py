from relationship_app.models import Author, Book, Library, Librarian

# Query all boks by a specific author
def get_books_by_author(author_name):
  author = Author.objects.get(name=author_name)
  return Book.objects.filter(author=author)

# List all books in a librery
def get_books_in_library(library_name):
  library = Library.objects.get(name=library_name)
  return library.books.all()

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
  library = Library.objects.get(name=library_name)
  return library.librarian

# Example 
author_name = "John Doe"
library_name = "Central Library"

books_by_author = get_books_by_author(author_name)
books_in_library = get_books_in_library(library_name)
librarian = get_librarian_for_library(library_name)

print(f"Books by {author_name}:")
for book in books_by_author:
  print(book.title)

print(f"\nBooks in {library_name}:")
for book in books_in_library:
  print(book.title)

print(f"\nLibrarian for {library_name}:")
print(librarian.name)
