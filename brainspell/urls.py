# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/',    include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
)

urlpatterns += patterns('website.views',
    url(r'^$', 'homepage', name='homepage'),
)

urlpatterns += patterns('papers.views',
    url(r'^paper/(?P<id>.+)$',   'paper',   name='paper'),
    url(r'^search$',             'search',  name='search'),
    url(r'^export$',             'export',  name='export'),
    url(r'^ajax_(?P<action>.+)', 'ajax_do', name='ajax_papers'),
)

urlpatterns += patterns('accounts.views',
    url(r'^register$',                'register',     name='register'),

    # url(r'^login$',                   'login',        name='login'),

    url(r'^logout$',                  'logout',       name='logout'),
    url(r'^forgot_password',          'forgot',       name='forgot'),
    url(r'^forgot_password/ok',       'forgot_ok',    name='forgot_ok'),
    url(r'^profile/(?P<member>.*)$',  'profile',      name='profile'),
    url(r'^profile$',                 'profile',      name='profile'),
)

urlpatterns += patterns('contents.views',
    url(r'^news/(?P<slug>.+)$', 'article', name='article'),
    url(r'^news$',              'news',    name='news'),
    url(r'^page/(?P<slug>.+)$', 'page',    name='page'),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve'),
)