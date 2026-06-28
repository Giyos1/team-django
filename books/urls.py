from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create_book_form/', views.book_create_form, name='create_form_book'),
    path('update_book_form/<int:pk>/', views.book_update_form, name='update_book_form'),
    path('create_book', views.book_create, name='create_book'),
    path('update_book/<int:pk>/', views.book_update, name='update_book'),
    path('delete_book/<int:pk>/', views.book_delete, name='delete_book'),
]
