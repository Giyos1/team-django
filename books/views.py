from django.shortcuts import render, redirect, get_object_or_404

from books.forms import BookForm, BookModelForm
from books.models import Books


def book_list(request):
    books = Books.objects.all()

    return render(request, 'books/list.html', context={"books": books})


def book_create_form(request):
    # form = BookForm()
    form = BookModelForm()
    return render(request, 'books/create.html', {"form": form})


def book_create(request):
    # form = BookForm(data=request.POST)
    form = BookModelForm(data=request.POST)
    if form.is_valid():
        # data = form.cleaned_data
        # Books.objects.create(
        #     name=data.get('name'),
        #     description=data.get('description'),
        #     price=data.get('price')
        # )
        form.save()
        return redirect('book_list')
    else:
        return render(request, 'books/create.html', {'form': form})


def book_update_form(request, pk):
    book = get_object_or_404(Books, id=pk)
    form = BookModelForm(instance=book)
    # form = BookModelForm(initial={
    #     'name': book.name,
    #     "description": book.description,
    #     'price': book.price
    # })
    return render(request, 'books/update.html', context={"book": book, 'form': form})


def book_update(request, pk):
    book = get_object_or_404(Books, id=pk)
    # book.name = request.POST.get('name')
    # book.description = request.POST.get('description')
    # book.price = request.POST.get('price')
    # book.save()
    form = BookModelForm(data=request.POST, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    else:
        return render(request, 'books/update.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Books, id=pk)
    if request.method == 'POST':
        book.delete()
    return redirect('book_list')


def book_detail(request, pk):
    book = get_object_or_404(Books, id=pk)
    return render(request, 'books/detail.html', context={"book": book})
