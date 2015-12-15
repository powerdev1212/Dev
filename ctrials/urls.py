# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$",views.ClinicalTrialsIndexView.as_view(),name="ctrials_index"),
]
