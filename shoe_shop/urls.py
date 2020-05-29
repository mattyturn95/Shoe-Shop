"""shoe_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from accounts import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_cart
from django.views import static
from .settings import MEDIA_ROOT
from search import urls as urls_search
from checkout import urls as urls_checkout
from products.views import all_products

from posts import urls as urls_posts
from posts.views import get_posts, post_detail, create_or_edit_post

from work import urls as urls_work
from work.views import work

from django.views import static
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_products, name='index'),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^work/', work, name='work'),
    url(r'^create_or_edit_post/', create_or_edit_post, name="create_or_edit_post"),
    url(r'^post_detail/', post_detail, name="post_detail"),
    url(r'^get_posts/', get_posts, name="get_posts"),
    url(r'^post$', RedirectView.as_view(url='posts/')),
    url(r'^posts/', include('posts.urls')),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
