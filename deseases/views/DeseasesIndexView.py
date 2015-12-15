# -*- coding: utf-8 -*-
from django.views.generic import ListView
from deseases.models import DeseaseType
from assets import views

class DeseasesIndexView(ListView):
    
    template_name = "deseases/index.html"
    
    def get_queryset(self):
        """ We want see categories with no parent only. """
        self.dtypes = DeseaseType.mgr.get_actives()

            
    def get_context_data(self, **kwargs):
        vdata = super(DeseasesIndexView, self).get_context_data(**kwargs)
        
        vdata["dtypes"] = self.dtypes
        return vdata
