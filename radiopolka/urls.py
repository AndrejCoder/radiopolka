"""radiopolka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include

from core.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^ckeditor/', include('django_ckeditor_5.urls')),
    re_path(r'^category/', include('core.category_urls'), name='category'),
    re_path(r'^publisher/', include('core.publisher_urls'), name='publisher'),
    re_path(r'^year/', include('core.year_urls'), name='year'),
    re_path(r'^book/', include('core.book_urls'), name='book')
]

admin.site.site_header = settings.ADMIN_SITE_HEADER
