# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = [
    url(r"^$",views.SearchResultsView.as_view(),name="search_index"),
]
