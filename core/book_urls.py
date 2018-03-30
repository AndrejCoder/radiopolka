from django.urls import re_path

from .views import BookDetailView, BooksByAlphaBetView

urlpatterns = [
    re_path(r'^(?P<slug>[a-z_A-Z0-9\-]*)/$', BookDetailView.as_view(), name='book-detail'),
    re_path(r'^alphabet/(?P<letter>[a-z_A-Z0-9\-]*)/$', BooksByAlphaBetView.as_view(), name='book-alphabet')
]