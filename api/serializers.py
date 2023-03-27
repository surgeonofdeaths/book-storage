from rest_framework import serializers

from book.models import Book


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'title', 'slug', 'content', 'cover', 'total_pages', 'pdf', 'language', 'published_date', 'isbn', 'user_id',
            'author_id', 'topics',
        )
