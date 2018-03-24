from django.conf import settings
from django.views.generic import TemplateView

from .api.book import BookApi
from .api.category import CategoryApi


class BaseTemplateView(TemplateView):
    template_engine = 'jinja2'
    template_file_name = ''

    def get_template_names(self):
        return ['themes/{0}/{1}.html'.format(settings.THEME_NAME, self.template_file_name)]


class IndexView(BaseTemplateView):
    template_file_name = 'index'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        category_list = CategoryApi.list()
        book_list = BookApi.list()

        context_data.update({
            'category_list': category_list,
            'book_list': book_list
        })

        return context_data


class BooksByCategoryView(BaseTemplateView):
    template_file_name = 'index'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        slug = kwargs.get('slug')

        category_list = CategoryApi.list()
        book_list = BookApi.list_by_category(slug)

        context_data.update({
            'category_list': category_list,
            'book_list': book_list
        })

        return context_data


class BookDetailView(BaseTemplateView):
    template_file_name = 'book_detail'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        slug = kwargs.get('slug')

        category_list = CategoryApi.list()
        book_detail = BookApi.detail(slug)

        context_data.update({
            'category_list': category_list,
            'book_detail': book_detail
        })

        return context_data
