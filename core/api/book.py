from core.dictionary import ALPHABET
from core.models import Book


class BookApi:

    @classmethod
    def list(cls):
        return Book.objects.all().order_by('created_date')

    @classmethod
    def list_by_category(cls, slug):
        return cls.list().filter(category__slug=slug)

    @classmethod
    def list_by_alphabet(cls, letter):
        if letter == '0-9':
            _filter = {'name__regex': r'^\d'}
        else:
            _filter = {'name__istartswith': ALPHABET.get(letter)}
        return cls.list().filter(**_filter)

    @classmethod
    def detail(cls, slug):
        return Book.objects.get(slug=slug)
