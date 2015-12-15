# -*- coding: utf-8 -*-
from django.views.generic import ListView
from ..models import Publication

class PublicationsIndexView(ListView):
    template_name = "publications/index.html"
    
    def get_queryset(self):
        """ We want see Publications as for desease requested. """
        self.items = Publication.objects.all()

            
    def get_context_data(self, **kwargs):
        vdata = super(PublicationsIndexView, self).get_context_data(**kwargs)
        vdata["items"] = self.items
        return vdata
