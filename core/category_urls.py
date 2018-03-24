from django.urls import re_path

from .views import BooksByCategoryView

urlpatterns = [
    re_path(r'^(?P<slug>[a-z_A-Z0-9\-]*)/$', BooksByCategoryView.as_view(), name='books-by-category')
]