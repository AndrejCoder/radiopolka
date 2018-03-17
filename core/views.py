from django.conf import settings
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_engine = 'jinja2'

    def get_template_names(self):
        return ['themes/{0}/index.html'.format(settings.THEME_NAME)]
