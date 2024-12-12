from django.urls import re_path

from .views import BooksByAuthorView

urlpatterns = [
    re_path(r'^(?P<slug>[a-z_A-Z0-9\-]*)/$', BooksByAuthorView.as_view(), name='books-by-author')
]
