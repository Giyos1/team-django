from django.contrib import admin
from django.urls import path, include

from books import views as books_views
from books.urls import book_urlpatterns, author_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', books_views.home, name='home'),
    path('books/', include(book_urlpatterns)),
    path('authors/', include(author_urlpatterns)),
]
