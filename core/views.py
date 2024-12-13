from django.conf import settings
from django.views.generic import TemplateView

from linkexchange_django.context_processors import linkexchange
from .api.author import AuthorApi
from .api.book import BookApi
from .api.category import CategoryApi
from .api.publisher import PublisherApi
from .dictionary import ALPHABET


class BaseTemplateView(TemplateView):
    template_engine = 'jinja2'
    template_file_name = ''

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update(linkexchange(self.request))
        context_data['alphabet_list'] = [{'key': k, 'value': v} for k, v in ALPHABET.items()]
        context_data['category_list'] = CategoryApi.list()
        context_data['author_list'] = AuthorApi.list()
        context_data['publisher_list'] = PublisherApi.list()
        context_data['book_year_list'] = BookApi.list_years()
        return context_data

    def get_template_names(self):
        return ['themes/{0}/{1}.html'.format(settings.THEME_NAME, self.template_file_name)]


class IndexView(BaseTemplateView):
    template_file_name = 'index'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        book_list = BookApi.list()

        context_data.update({
            'book_list': book_list,
            'title': 'Перечень книг',
            'tab_title': ''
        })
        return context_data


class BooksByCategoryView(BaseTemplateView):
    template_file_name = 'index'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        slug = kwargs.get('slug')

        category = CategoryApi.by_pk(slug)
        book_list = BookApi.list_by_category(slug)
        title = f'Перечень книг категории «{category.name}»'

        context_data.update({
            'book_list': book_list,
            'title': title,
            'tab_title': title
        })
        return context_data


class BookDetailView(BaseTemplateView):
    template_file_name = 'book_detail'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        slug = kwargs.get('slug')
        book_detail = BookApi.detail(slug)

        context_data.update({
            'book_detail': book_detail,
            'title': book_detail.name,
            'tab_title': '{0} - {1}'.format(book_detail.author_str, book_detail.name)
        })
        return context_data


class BooksByAlphaBetView(BaseTemplateView):
    template_file_name = 'index'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        letter = kwargs.get('letter')
        book_list = BookApi.list_by_alphabet(letter)

        if letter == '0-9':
            title = 'Перечень книг, начинающихся на цифру'
        else:
            title = 'Перечень книг, начинающихся на букву «{0}»'.format(ALPHABET.get(letter))

        context_data.update({
            'book_list': book_list,
            'title': title,
            'tab_title': title
        })
        return context_data


class BooksByPublisherView(BaseTemplateView):
    template_file_name = 'index'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        slug = kwargs.get('slug')
        publisher = PublisherApi.by_pk(slug)
        book_list = BookApi.list_by_publisher(slug)
        title = f'Перечень книг издательства «{publisher.name}»'

        context_data.update({
            'book_list': book_list,
            'title': title,
            'tab_title': title
        })
        return context_data


class BooksByYearView(BaseTemplateView):
    template_file_name = 'index'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        year = kwargs.get('year')
        book_list = BookApi.list_by_year(year)

        title = f'Перечень книг {year} года издания'

        context_data.update({
            'book_list': book_list,
            'title': title,
            'tab_title': title
        })
        return context_data


class BooksByAuthorView(BaseTemplateView):
    template_file_name = 'index'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        slug = kwargs.get('slug')
        author = AuthorApi.by_pk(slug)
        book_list = BookApi.list_by_author(slug)

        title = f'Перечень книг автора {author}'

        context_data.update({
            'book_list': book_list,
            'title': title,
            'tab_title': title
        })
        return context_data
