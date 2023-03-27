from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from common.utils import DataMixin
from .mixins import BookPermissionMixin

from .models import Book


class HomeTemplateView(DataMixin, TemplateView):
    template_name = 'book/home.html'

    def get_context_data(self, **kwargs):
        new_context = {'title': 'Home Page', 'selected': 'home'}
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

    def get_queryset(self):
        return Book.objects.all().prefetch_related('topics')


class BookDetailView(LoginRequiredMixin, DataMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book/book_detail.html'

    def get_context_data(self, **kwargs):
        new_context = {'title': kwargs.get('object').title, 'selected': 'books'}
        context = super().get_context_data(**new_context, **kwargs)
        return context


class AboutTemplateView(DataMixin, TemplateView):
    template_name = 'book/about.html'

    def get_context_data(self, **kwargs):
        new_context = {'title': 'About', 'selected': 'about'}
        context = super().get_context_data(**new_context, **kwargs)
        return context


class EditBookUpdateView(LoginRequiredMixin, BookPermissionMixin, DataMixin, UpdateView):
    model = Book
    template_name = 'book/book_edit.html'
    fields = (
        'title', 'content', 'cover', 'total_pages', 'pdf', 'language', 'isbn', 'topics', 'author'
    )

    def get_context_data(self, **kwargs):
        new_context = {'title': f'Edit "{self.object.title}"', 'selected': 'books'}
        context = super().get_context_data(**new_context, **kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'slug': self.object.slug})


class DeleteBookView(LoginRequiredMixin, BookPermissionMixin, DataMixin, DeleteView):
    model = Book
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('books')

    def get_context_data(self, **kwargs):
        new_context = {'title': 'Are you sure you want to delete this book?', 'selected': 'books'}
        context = super().get_context_data(**new_context, **kwargs)
        return context


class PublishBookCreateView(LoginRequiredMixin, DataMixin, CreateView):
    model = Book
    template_name = 'book/book_publish.html'
    fields = (
        'title', 'content', 'cover', 'total_pages', 'pdf', 'language', 'isbn', 'topics', 'author'
    )

    def get_context_data(self, **kwargs):
        new_context = {'title': 'Publish Book', 'selected': 'book_publish'}
        context = super().get_context_data(**new_context, **kwargs)
        return context


    # def get_success_url(self):
    #     return reverse_lazy('book_detail', kwargs={'slug': self.})