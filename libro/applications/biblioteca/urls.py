from django.urls import path, re_path

from . import views

app_name="biblioteca_app"

urlpatterns = [
    path('', views.AuthorsList.as_view(), name="authors"),
    path('books-author-list/<id>/', views.AuthorBooksList.as_view(), name="books-author"),
    path('author/add', views.AddAuthor.as_view(), name="add-author"),
]