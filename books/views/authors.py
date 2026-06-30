from books.forms import AuthorModelForm
from books.models import Authors
from django.shortcuts import render, redirect, get_object_or_404



def authors_list(request):
    authors = Authors.objects.all()
    return render(
        request,
        'authors/list.html',
        context={"authors": authors}
    )

def author_create_form(request):
    form = AuthorModelForm()
    return render(request, 'authors/create.html', {"form": form})

def author_create(request):
    if request.method == "POST":
        form = AuthorModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("authors_list")
        print(form.errors)
    else:
        form = AuthorModelForm()
    return render(request, "authors/create.html", {"form": form})

def author_update_form(request, pk):
    author = get_object_or_404(Authors, pk=pk)
    form = AuthorModelForm(instance=author)
    return render(request,'authors/update.html',{"author": author,"form": form})

def author_update(request, pk):
    if request.method != "POST":
        return redirect("update_author_form", pk=pk)
    author = get_object_or_404(Authors, pk=pk)
    form = AuthorModelForm(request.POST, request.FILES, instance=author)
    if form.is_valid():
        form.save()
        return redirect("authors_list")
    return render(request, "authors/update.html", {"author": author,"form": form})

def author_delete(request, pk):
    author = get_object_or_404(Authors, pk=pk)
    if request.method == "POST":
        author.delete()
    return redirect("authors_list")

def author_detail(request, pk):
    author = get_object_or_404(Authors, id=pk)
    return render(request, 'authors/detail.html', context={"author": author})
