from django.conf import settings
from django.views.generic import TemplateView

from .api.book import BookApi
from .api.category import CategoryApi


class IndexView(TemplateView):
    template_engine = 'jinja2'

    def get_template_names(self):
        return ['themes/{0}/index.html'.format(settings.THEME_NAME)]

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        category_list = CategoryApi.list()
        book_list = BookApi.list()

        context_data.update({
            'category_list': category_list,
            'book_list': book_list
        })

        return context_data
