from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('books/', BookListView.as_view(), name='books'),
    path('books/<slug:slug>', BookDetailView.as_view(), name='book_detail'),
]
