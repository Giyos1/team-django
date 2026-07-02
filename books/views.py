from django.shortcuts import render, redirect, get_object_or_404

from books.forms import BookModelForm, AuthorsModelForm
from books.models import Books, Authors


def home(request):
    return render(request, 'home.html')


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




def authors_list(request):
    authors = Authors.objects.all()

    return render(request, 'authors/list.html', context={"authors": authors})

def author_create_form(request):
    form = AuthorsModelForm()
    return render(request, 'authors/create.html', {"form": form})


def author_create(request):
    form = AuthorsModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('author_list')
    else:
        return render(request, 'authors/create.html', {'form': form})


def author_detail(request, pk):
    author = get_object_or_404(Authors, id=pk)
    return render(request, 'authors/detail.html', context={"author": author})


def author_update_form(request, pk):
    author = get_object_or_404(Authors, id=pk)
    form = AuthorsModelForm(instance=author)
    return render(request, 'authors/update.html', context={"author": author, 'form': form})


def author_update(request, pk):
    author = get_object_or_404(Authors, id=pk)
    form = AuthorsModelForm(data=request.POST, instance=author)
    if form.is_valid():
        form.save()
        return redirect('author_list')
    else:
        return render(request, 'authors/update.html', {'author': author, 'form': form})


def author_delete(request, pk):
    author = get_object_or_404(Authors, id=pk)
    if request.method == 'POST':
        author.delete()
    return redirect('author_list')

