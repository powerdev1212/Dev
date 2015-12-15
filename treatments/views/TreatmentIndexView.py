# -*- coding: utf-8 -*-
from django.views.generic import ListView
from ..models import Treatment

class TreatmentIndexView(ListView):
    template_name = "treatments/index.html"
    
    def get_queryset(self):
        """ We want see Treatment info as for desease requested. """
        self.items = Treatment.mgr.get_by_deseases_mnemo(self.kwargs.get("lev2", False))

            
    def get_context_data(self, **kwargs):
        vdata = super(TreatmentIndexView, self).get_context_data(**kwargs)
        vdata["items"] = self.items
        return vdata
