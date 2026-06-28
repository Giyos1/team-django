from django.contrib import admin
from .models import Authors, Books

admin.site.register(Authors)


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]
