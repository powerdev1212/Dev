# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from deseases.views import LoginView
from django.views.generic import TemplateView
from deseases.views import HomeView

admin.autodiscover()

urlpatterns = i18n_patterns('',
    #url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^browse/', include('deseases.urls')), # deseases section
    url(r'^search/', include('search.urls')), # search section
    url(r'^login/$', LoginView.as_view(), name='login'), # login section
    url(r'^logout/$', 'deseases.views.logoutview', name='logout'), # login section
    url(r"^api/experts/json/$", "api.views.experts_list_json"),
    url(r"^api/experts/(?P<expert_id>[0-9]+)/json/$", "api.views.expert_instance_json"),
    url(r'^', include('cms.urls')),
    #url(r'^', HomeView.as_view(), name='home'),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^files/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA
