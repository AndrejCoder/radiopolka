from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'theme_stylesheet_url': settings.THEME_STYLESHEET_URL,
        'theme_javascript_url': settings.THEME_JAVASCRIPT_URL,
        'theme_image_url': settings.THEME_IMAGE_URL,
        'image_url': settings.IMAGE_URL,
        'book_url': settings.BOOK_URL
    })
    return env
