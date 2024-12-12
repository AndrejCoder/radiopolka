from core.models import Author


class AuthorApi:

    @classmethod
    def list(cls):
        return Author.objects.all().order_by('name')

    @classmethod
    def by_pk(cls, pk):
        return cls.list().get(pk=pk)
