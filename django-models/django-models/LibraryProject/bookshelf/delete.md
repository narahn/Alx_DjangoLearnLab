booktodelete=Book.objects.get(id=1)
booktodelete.delete()
(1, {'bookshelf.Book': 1})
book.delete", "from bookshelf.models import Book"