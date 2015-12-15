# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = [
    url(r"^$",views.TreatmentIndexView.as_view(),name="treatment_index"),
    url(r"^(?P<lev4>[0-9a-z\_\-]+)/$",views.TreatmentGuidelineView.as_view(),name="treatment_guideline"),
]
