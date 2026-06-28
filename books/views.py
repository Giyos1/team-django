from django.shortcuts import render, redirect, get_object_or_404

from books.models import Books


def book_list(request):
    books = Books.objects.all()

    return render(request, 'books/list.html', context={"books": books})


def book_create_form(request):
    return render(request, 'books/create.html')


def book_create(request):
    data = request.POST
    Books.objects.create(
        name=data.get('name'),
        description=data.get('description'),
        price=data.get('price')
    )
    return redirect('book_list')


def book_update_form(request, pk):
    book = get_object_or_404(Books, id=pk)
    return render(request, 'books/update.html', context={"book": book})
