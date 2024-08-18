from django.urls import path
from .views import list_books  # Import the list_books function
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
  path('books/', list_books, name='list_books'),
  path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
  path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
  path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
  path('register/', views.register_view, name='register'),
]
