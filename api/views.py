from rest_framework import generics, views

from book.models import Book
from .serializers import *


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
