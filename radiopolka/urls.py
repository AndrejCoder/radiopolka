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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from core.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^category/', include('core.category_urls'), name='category'),
    url(r'^book/', include('core.book_urls'), name='book')
]

admin.site.site_header = settings.ADMIN_SITE_HEADER
