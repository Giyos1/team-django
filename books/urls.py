from django.urls import path
from . import views

book_urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create_book_form/', views.book_create_form, name='create_form_book'),
    path('update_book_form/<int:pk>/', views.book_update_form, name='update_book_form'),
    path('create_book', views.book_create, name='create_book'),
    path('update_book/<int:pk>/', views.book_update, name='update_book'),
    path('delete_book/<int:pk>/', views.book_delete, name='delete_book'),

    path('detail_book/<int:pk>/', views.book_detail, name='detail_book'),
]

author_urlpatterns = [
    path('', views.authors_list, name='author_list'),
    path('create_author_form/', views.author_create_form, name='create_form_author'),
    path('create_author', views.author_create, name='create_author'),
    path('update_author_form/<int:pk>/', views.author_update_form, name='update_author_form'),
    path('update_author/<int:pk>/', views.author_update, name='update_author'),
    path('delete_author/<int:pk>/', views.author_delete, name='delete_author'),

    path('detail_author/<int:pk>/', views.author_detail, name='detail_author'),
]
