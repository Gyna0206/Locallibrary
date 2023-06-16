from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

# Create your views here.
from ..models import Book, Author, BookInstance


def index(request):
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits']=num_visits+1
    context={
            'num_books':num_books, 
            'num_instances':num_instances,
            'num_instances_available':num_instances_available,
            'num_authors':num_authors,
            'num_visits': num_visits,
        }
    return render(
        request,
        'index.html', context=context
       
    )
  # books = Book.objects.all()

    # return render(
    #     request, 
    #     'index.html',
    #     context={
    #         "libros":books,

    #     }
                                
    # )
class BookListView(generic.ListView):
    model=Book
    context_object_name = 'book_list'
    template_name = 'catalog/book_list.html'
    paginate_by = 10
    #def get_queryset(self):
        #return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war

class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model= Author
    context_object_name = 'author_list'
    template_name='catalog/author_list.html'
    def get_queryset(self):
        return Author.objects.order_by()
        

class AuthorDetailView(generic.DetailView):
    model = Author
