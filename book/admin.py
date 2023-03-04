from django.contrib import admin

from .models import Author, Topic, Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'author', 'language']
    list_editable = ['language']
    list_per_page = 10
    list_display_links = ['title', 'user', 'author']
    search_fields = ['title', 'user', 'author']
    prepopulated_fields = {'slug': ('title', )}
    ordering = ['title', 'author', 'user']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name']
    list_display_links = ['first_name', 'middle_name', 'last_name']
    ordering = ['first_name', 'middle_name', 'last_name']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    list_per_page = 10
    search_fields = ['name']
    ordering = ['name']
