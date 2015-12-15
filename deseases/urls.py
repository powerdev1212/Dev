# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = [
    url(r"^$", views.DeseasesIndexView.as_view(), name="deseases_index"),
    url(r"^(?P<lev0>[0-9a-z\_\-]+)/$",
        views.DeseasesTypeView.as_view(),
        name="deseases_type"),
    url(r"^(?P<lev0>[0-9a-z\_\-]+).json/$",
        views.DeseasesTypeJSONView.as_view(),
        name="deseases_type_json"),
    url(r"^(?P<lev0>[0-9a-z\_\-]+)/(?P<lev1>[0-9a-z\_\-]+)/$",
        views.DeseasesCategoryView.as_view(),
        name="deseases_category"),
    url(r"^(?P<lev0>[0-9a-z\_\-]+)/(?P<lev1>[0-9a-z\_\-]+)/(?P<lev2>[0-9a-z\_\-\,\:]+)/$",
        views.DeseaseItemView.as_view(),
        name="desease_item"),
    url(r"^(?P<lev0>[0-9a-z\_\-]+)/(?P<lev1>[0-9a-z\_\-]+)/(?P<lev2>[0-9a-z\_\-\,\:]+)/(?P<lev3>[0-9a-z\_\-\,\:]+)/$",
        views.DeseaseItemView.as_view(),
        name="desease_item")
]
