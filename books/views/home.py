from django.db.models import Avg
from django.shortcuts import render

from books.models import Books, Authors


def home(request):
    context = {
        "books_count": Books.objects.count(),
        "authors_count": Authors.objects.count(),
        "average_price": Books.objects.aggregate(
            avg=Avg("price")
        )["avg"] or 0,
        "latest_books": Books.objects.select_related("author").order_by("-id")[:5],
        "latest_authors": Authors.objects.order_by("-id")[:5],
    }

    return render(request, "home.html", context)
