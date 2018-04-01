from django.conf import settings
from django.views.generic import TemplateView

from .api.book import BookApi
from .api.category import CategoryApi
from .dictionary import ALPHABET


class BaseTemplateView(TemplateView):
    template_engine = 'jinja2'
    template_file_name = ''

    def get_template_names(self):
        return ['themes/{0}/{1}.html'.format(settings.THEME_NAME, self.template_file_name)]


class IndexView(BaseTemplateView):
    template_file_name = 'index'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        alphabet_list = list()
        for k, v in ALPHABET.items():
            alphabet_list.append({'key': k, 'value': v})

        category_list = CategoryApi.list()
        book_list = BookApi.list()

        context_data.update({
            'category_list': category_list,
            'book_list': book_list,
            'alphabet_list': alphabet_list,
            'title': 'Перечень книг',
            'tab_title': ''
        })

        return context_data


class BooksByCategoryView(BaseTemplateView):
    template_file_name = 'index'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        slug = kwargs.get('slug')

        alphabet_list = list()
        for k, v in ALPHABET.items():
            alphabet_list.append({'key': k, 'value': v})

        category = CategoryApi.by_pk(slug)
        category_list = CategoryApi.list()
        book_list = BookApi.list_by_category(slug)

        context_data.update({
            'category_list': category_list,
            'book_list': book_list,
            'alphabet_list': alphabet_list,
            'title': 'Перечень книг категории «{0}»'.format(category.name),
            'tab_title': 'Перечень книг категории «{0}»'.format(category.name)
        })

        return context_data


class BookDetailView(BaseTemplateView):
    template_file_name = 'book_detail'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        slug = kwargs.get('slug')

        alphabet_list = list()
        for k, v in ALPHABET.items():
            alphabet_list.append({'key': k, 'value': v})

        category_list = CategoryApi.list()
        book_detail = BookApi.detail(slug)

        context_data.update({
            'category_list': category_list,
            'book_detail': book_detail,
            'alphabet_list': alphabet_list,
            'title': book_detail.name,
            'tab_title': '{0} - {1}'.format(book_detail.author_str, book_detail.name)
        })

        return context_data


class BooksByAlphaBetView(BaseTemplateView):
    template_file_name = 'index'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        letter = kwargs.get('letter')

        alphabet_list = list()
        for k, v in ALPHABET.items():
            alphabet_list.append({'key': k, 'value': v})

        category_list = CategoryApi.list()
        book_list = BookApi.list_by_alphabet(letter)

        if letter == '0-9':
            title = 'Перечень книг, начинающихся на цифру'
        else:
            title = 'Перечень книг, начинающихся на букву «{0}»'.format(ALPHABET.get(letter))

        context_data.update({
            'category_list': category_list,
            'book_list': book_list,
            'alphabet_list': alphabet_list,
            'title': title,
            'tab_title': title
        })

        return context_data
