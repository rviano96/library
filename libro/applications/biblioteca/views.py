from applications.biblioteca.models import Author
from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
)

from .models import Author, Book

class AuthorsList(ListView):
    template_name = "biblioteca/authors-list.html"
    model = Author
    context_object_name = 'authors'

#View to list books by author
class AuthorBooksList(ListView):
    template_name = "biblioteca/books-list.html"
    context_object_name = 'books'

    def get_queryset(self):
        # Identify the author
        id = self.kwargs['id'] #From url get the arg 'id'
        # Filter books by author
        books = Book.objects.filter(
            author=id
        )
        # Return results
        return books
    
class AddAuthor(CreateView):
    """View to add new author"""
    template_name = 'biblioteca/add-author.html'
    model = Author
    fields = ['name', 'nationality']
    success_url =  '/' #This reload the page when author is added.
