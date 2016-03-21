__author__ = 'casey'

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.researcher, name='researcher'),
    url(r'^search/(?P<pk>\d+)/$', views.search_previous, name='search_previous'),
    url(r'^search/$', views.search_detail, name='search_detail'),
]