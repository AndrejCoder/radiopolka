from django.urls import re_path

from .views import BooksByPublisherView

urlpatterns = [
    re_path(r'^(?P<slug>[a-z_A-Z0-9\-]*)/$', BooksByPublisherView.as_view(), name='books-by-publisher')
]