from django.db.models import ForeignKey, SlugField, CharField, CASCADE, Model, IntegerField, TextField
from mptt.models import MPTTModel


class Category(MPTTModel):
    slug = SlugField(verbose_name='Код категории', primary_key=True)
    parent = ForeignKey(to='self', verbose_name='Родитель', blank=True, null=True, db_index=True, on_delete=CASCADE)
    name = CharField(verbose_name='Наименование категори', max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Author(Model):
    slug = SlugField(verbose_name='Код автора', primary_key=True)
    name = CharField(verbose_name='Автор', max_length=255)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return '{0}'.format(self.name)


class Publisher(Model):
    slug = SlugField(verbose_name='Код издательства', primary_key=True)
    name = CharField(verbose_name='Издательство', max_length=150)

    class Meta:
        verbose_name = 'Издательство'
        verbose_name_plural = 'Издательства'


class Language(Model):
    slug = SlugField(verbose_name='Код языка издания', primary_key=True)
    name = CharField(verbose_name='Язык издания', max_length=150)

    class Meta:
        verbose_name = 'Язык издания'
        verbose_name_plural = 'Языки изданий'


class Type(Model):
    slug = SlugField(verbose_name='Код типа издания', primary_key=True)
    name = CharField(verbose_name='Тип издания', max_length=50)

    class Meta:
        verbose_name = 'Тип издания'
        verbose_name_plural = 'Типы изданий'


class Book(Model):
    slug = SlugField(verbose_name='Код книги')
    name = CharField(verbose_name='Название книги', max_length=255)
    category = ForeignKey(to=Category, verbose_name='Категория', on_delete=CASCADE, related_name='category_books')
    author = ForeignKey(to=Author, verbose_name='Автор', on_delete=CASCADE, related_name='author_books')
    format = CharField(verbose_name='Формат издания', max_length=100, blank=True, null=True)
    pages = IntegerField(verbose_name='Количество страниц')
    year = IntegerField(verbose_name='Год издания')
    publisher = ForeignKey(to=Publisher, verbose_name='Издательство', on_delete=CASCADE, related_name='publisher_books')
    cover = CharField(verbose_name='Переплёт', max_length=100)
    language = ForeignKey(to=Language, verbose_name='Язык издания', on_delete=CASCADE, related_name='language_books')
    type = ForeignKey(to=Type, verbose_name='Тип издания', on_delete=CASCADE, related_name='type_books', blank=True,
                      null=True)
    weight = IntegerField(verbose_name='Вес')
    description_big = TextField(verbose_name='Описание (полное)')
    description_small = TextField(verbose_name='Описание короткое')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return '{0} - {1}'.format(self.author, self.name)
