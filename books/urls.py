from django.urls import path
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

urlpatterns = [
    path('', book_list, name='book_list'),
    path('create_book_form/', book_create_form, name='create_form_book'),
    path('update_book_form/<int:pk>/', book_update_form, name='update_book_form'),
    path('create_book', book_create, name='create_book'),
    path('update_book/<int:pk>/', book_update, name='update_book'),
    path('delete_book/<int:pk>/', book_delete, name='delete_book'),
    path('detail_book/<int:pk>/', book_detail, name='detail_book'),
    path('authors/', authors_list, name='authors_list'),
    path('create-author_form', author_create_form, name='create_from_author'),
    path('create_author', author_create, name='create_author'),
    path('update-author-form/<int:pk>/', author_update_form, name='update_author_form'),
    path('update-author/<int:pk>/', author_update,name='update_author'),
    path('delete_author/<int:pk>/', author_delete, name='delete_author'),
    path('detail_author/<int:pk>/', author_detail, name='detail_author'),
]
