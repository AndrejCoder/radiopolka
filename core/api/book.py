from core.models import Book


class BookApi:

    @classmethod
    def list(cls):
        return Book.objects.all()

    @classmethod
    def list_by_category(cls, slug):
        return cls.list().filter(category__slug=slug)

    @classmethod
    def detail(cls, slug):
        return Book.objects.get(slug=slug)
