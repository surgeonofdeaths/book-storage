from django.views.generic import TemplateView, ListView, DetailView
from .models import Book


class HomeTemplateView(TemplateView):
    template_name = '_base.html'


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book/book_list.html'


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book/book_detail.html'


class AboutTemplateView(TemplateView):
    template_name = 'book/about.html'
