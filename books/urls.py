from django.urls import path
from . import views

urlpatterns = [
    path('books', views.books, name='books'),
    path('create', views.create, name="create"),
    path('shelf', views.shelf, name='shelf'),
]
