from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'stylesheet_url': settings.THEME_STYLESHEET_URL,
        'javascript_url': settings.THEME_JAVASCRIPT_URL,
        'image_url': settings.THEME_IMAGE_URL
    })
    return env
