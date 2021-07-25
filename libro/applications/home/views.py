from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    ListView
)


class IndexView(TemplateView):
    #Una vista procesa los datos y renderiza el resultado en pantalla.
    #Siempre pedira un template.
    #Un template es un archivo html
    template_name = "home/index.html"

class BooksList(ListView):
    template_name = "home/list.html"
    #Should get list from db
    queryset = ['El quijote', 'Sherlock Holmes', 'Da Vinci Code', 'Django 3.2.5']  
    context_object_name = 'books'
