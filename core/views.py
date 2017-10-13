from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_engine = 'jinja2'
    template_name = 'index.html'
