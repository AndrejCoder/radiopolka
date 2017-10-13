from django.contrib import admin

from .models import Category, Author, Publisher, Language, Type, Book


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']
    list_per_page = 50


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']
    list_per_page = 50


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']
    list_per_page = 50


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']
    list_per_page = 50


class TypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']
    list_per_page = 50


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'category', 'publisher']
    search_fields = ['name', 'author__name', 'category__name', 'publisher__name']
    list_per_page = 50


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Book, BookAdmin)
