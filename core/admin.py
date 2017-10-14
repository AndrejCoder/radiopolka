from django.contrib import admin
from django.utils.safestring import mark_safe

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
    list_display = ['name', 'author_list', 'category', 'publisher']
    search_fields = ['name', 'author__name', 'category__name', 'publisher__name']
    list_per_page = 50

    def author_list(self, obj):
        return mark_safe("<br/>".join(obj.author.all().values_list('name', flat=True)))

    author_list.short_description = 'Авторы'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Book, BookAdmin)
