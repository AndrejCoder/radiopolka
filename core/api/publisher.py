from core.models import Publisher


class PublisherApi:

    @classmethod
    def list(cls):
        return Publisher.objects.all().order_by('name')

    @classmethod
    def by_pk(cls, pk):
        return cls.list().get(pk=pk)