from django.urls import path
from .views import list_books  # Import the list_books function

urlpatterns = [
  path('books/', list_books, name='list_books'),
  path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]