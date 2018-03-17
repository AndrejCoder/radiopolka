from core.models import Category


class CategoryApi:

    @classmethod
    def list(cls):
        return Category.objects.all()