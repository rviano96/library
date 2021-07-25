from django.contrib import admin

# Register your models here.
from .models import Author, Book


# Clase para mejorar el admin de autor
class AdminAuthor(admin.ModelAdmin):
    list_display = (
        'name',
        'nationality',
        'id'
    )
    # Attributo para buscar por campo
    search_fields = ('name', 'nationality',)

    # Clase para mejorar el admin de libros
class AdminBook(admin.ModelAdmin):
    list_display = (
        'title',
        'resume',
        'author',
        'id'
    )

    # Attributo para buscar por campo
    search_fields = ('title',)
    
    #Filter results
    list_filter = ('author',)

admin.site.register(Author, AdminAuthor)
admin.site.register(Book, AdminBook)