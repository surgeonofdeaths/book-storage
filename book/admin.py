from django.contrib import admin

from .models import Author, Genre, Book


class BookInline(admin.TabularInline):
    model = Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'author', 'language']
    list_editable = ['language']
    list_per_page = 10
    list_display_links = ['title', 'user', 'author']
    search_fields = ['title', 'user', 'author']
    ordering = ['title', 'author', 'user']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]
    list_display = ['first_name', 'last_name']
    list_display_links = ['first_name', 'last_name']
    ordering = ['first_name', 'last_name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre_name']
    list_display_links = ['genre_name']
    list_per_page = 10
    search_fields = ['genre_name']
    ordering = ['genre_name']
