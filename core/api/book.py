from core.models import Book


class BookApi:

    @classmethod
    def list(cls):
        return Book.objects.all()