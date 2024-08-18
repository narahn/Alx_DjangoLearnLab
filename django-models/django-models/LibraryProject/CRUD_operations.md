from bookshelf.models import Book
new_book = Book(title = '1984' , author = 'George Orwell' , publication_year = '1949')
new_book.save()
all_books=Book.objects.all()
print(all_books)
<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>]>
book_to_update = Book.objects.get(id=2)
book_to_update.title='Nineteen Eighty-Four'
booktodelete=Book.objects.get(id=1)
booktodelete.delete()
(1, {'bookshelf.Book': 1})