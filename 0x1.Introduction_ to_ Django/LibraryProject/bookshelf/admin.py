from django.contrib import admin

# Register your models here.
from .models import Book



# Register the Book model with the admin site using the custom class
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author',)  # Filter by author
    search_fields = ('title', 'author',)  # Search by title and author
admin.site.register(Book, BookAdmin)
