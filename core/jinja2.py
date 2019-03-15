from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def sape():
    from linkexchange.clients.sape import SapeClient
    clients = [
        SapeClient(
            user='c147e46648d8cbbe8d21a7bdd550415a',
            db_driver=(
                'shelve',
                [],
                   dict(
                       filename='/home/abelov/sape/sape-XXX.db'
                   )
                       ))]
    from linkexchange.platform import Platform
    platform = Platform(clients)
    from linkexchange.clients import PageRequest
    req = PageRequest(host='radiopolka.ru', uri='/book/radioelektronika-dlya-chainikov-2007/')
    lx = platform.get_raw_links(req)
    return lx


def environment(**options):
    env = Environment(**options)
    sape_links = sape()
    print(sape_links[0].link_code)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'theme_stylesheet_url': settings.THEME_STYLESHEET_URL,
        'theme_javascript_url': settings.THEME_JAVASCRIPT_URL,
        'theme_image_url': settings.THEME_IMAGE_URL,
        'image_url': settings.IMAGE_URL,
        'book_url': settings.BOOK_URL,
        'sape_links': sape_links[0].link_code if sape_links else ''
    })
    return env
