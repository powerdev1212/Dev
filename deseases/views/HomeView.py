from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext

class HomeView(TemplateView):
    template_name = "deseases/index.html"

