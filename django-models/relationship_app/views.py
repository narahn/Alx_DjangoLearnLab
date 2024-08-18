from django.shortcuts import render , redirect
from .models import Book , Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test



def list_books(request):
  """Displays a list of all books in the database."""
  books = Book.objects.all()
  context = {'books': books}
  return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'


def register_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()

      # Redirect to login page or other success view after registration
      return redirect('login')
  else:
    form = UserCreationForm()
  return render(request, 'relationship_app/register.html', {'form': form})

def login_view(request):
  if request.method == 'POST':
    # Handle login logic using request.POST data (username and password)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      # Redirect to   successful login page
      return redirect('list_books')  # Or another protected view
    else:
      # Handle invalid login attempt (e.g., display error message)
        return render(request, 'relationship_app/login.html')  # Or custom login template

def logout_view(request):
  logout(request)
  return redirect('login')
def Admin_view(request):
    # Only accessible to users with the 'Admin' role
    return render(request, 'admin_view.html')

def librarian_view(request):
    # Only accessible to users with the 'Librarian' role
    return render(request, 'librarian_view.html')

def member_view(request):
    # Only accessible to users with the 'Member' role
    return render(request, 'member_view.html')

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

Admin_view = user_passes_test(is_admin)(Admin_view)
librarian_view = user_passes_test(is_librarian)(librarian_view)
member_view = user_passes_test(is_member)(member_view)