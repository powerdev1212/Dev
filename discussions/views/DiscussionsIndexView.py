# -*- coding: utf-8 -*-
from django.views.generic import ListView
from ..models import Discussion

class DiscussionsIndexView(ListView):
    template_name = "discussions/index.html"
    
    def get_queryset(self):
        """ We want see Discussions as for desease requested. """
        self.items = Discussion.objects.all()

            
    def get_context_data(self, **kwargs):
        vdata = super(DiscussionsIndexView, self).get_context_data(**kwargs)
        vdata["items"] = self.items
        return vdata
