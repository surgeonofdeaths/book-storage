from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book
from common.utils import DataMixin


class HomeTemplateView(DataMixin, TemplateView):
    template_name = '_base.html'

    def get_context_data(self, **kwargs):
        new_context = {'title': 'Home Page'}
        context = super().get_context_data(**new_context, **kwargs)
        return context


class BookListView(LoginRequiredMixin, DataMixin, ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book/book_list.html'

    def get_context_data(self, **kwargs):
        new_context = {'title': 'All Books', 'selected': 'books'}
        context = super().get_context_data(**new_context, **kwargs)
        return context


class BookDetailView(LoginRequiredMixin, DataMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book/book_detail.html'

    def get_context_data(self, **kwargs):
        new_context = {'title': self.request.POST, 'selected': 'books'}
        context = super().get_context_data(**new_context, **kwargs)
        return context


class AboutTemplateView(DataMixin, TemplateView):
    template_name = 'book/about.html'

    def get_context_data(self, **kwargs):
        new_context = {'title': 'About', 'selected': 'about'}
        context = super().get_context_data(**new_context, **kwargs)
        return context
