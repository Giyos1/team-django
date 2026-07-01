from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from books.views.authors import author_create_form, author_create, authors_list, author_update_form, author_update, \
    author_delete, author_detail
from books.views.books import (
    book_list,
    book_create_form,
    book_update_form,
    book_create,
    book_update,
    book_delete,
    book_detail
)
from books.views.home import home

urlpatterns = [
    # Home
    path("", home, name="home"),

    # Books
    path("books/", book_list, name="book_list"),
    path("books/create/", book_create_form, name="create_form_book"),
    path("books/store/", book_create, name="create_book"),
    path("books/<int:pk>/", book_detail, name="detail_book"),
    path("books/<int:pk>/edit/", book_update_form, name="update_book_form"),
    path("books/<int:pk>/update/", book_update, name="update_book"),
    path("books/<int:pk>/delete/", book_delete, name="delete_book"),

    # Authors
    path("authors/", authors_list, name="authors_list"),
    path("authors/create/", author_create_form, name="create_from_author"),
    path("authors/store/", author_create, name="create_author"),
    path("authors/<int:pk>/", author_detail, name="detail_author"),
    path("authors/<int:pk>/edit/", author_update_form, name="update_author_form"),
    path("authors/<int:pk>/update/", author_update, name="update_author"),
    path("authors/<int:pk>/delete/", author_delete, name="delete_author"),
]
