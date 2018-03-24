from django.urls import re_path

from .views import BookDetailView

urlpatterns = [
    re_path(r'^(?P<slug>[a-z_A-Z0-9\-]*)/$', BookDetailView.as_view(), name='book-detail')
]