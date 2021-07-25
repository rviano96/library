from django.urls import path, re_path

from . import views

app_name="home_app"

urlpatterns = [
    path('index', views.IndexView.as_view(), name="index"),
    path('books-list', views.BooksList.as_view(), name="list"),
]