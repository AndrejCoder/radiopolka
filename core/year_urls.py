from django.urls import re_path

from .views import BooksByYearView

urlpatterns = [
    re_path(r'^(?P<year>[0-9]*)/$', BooksByYearView.as_view(), name='books-by-year')
]