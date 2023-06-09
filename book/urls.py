from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('books/', BookListView.as_view(), name='books'),
    path('books/<slug:slug>', BookDetailView.as_view(), name='book_detail'),
    path('books/edit/<slug:slug>', EditBookUpdateView.as_view(), name='book_edit'),
    path('books/delete/<slug:slug>', DeleteBookView.as_view(), name='book_delete'),
    path('books/publish/', PublishBookCreateView.as_view(), name='publish_book'),
]

