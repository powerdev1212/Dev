# -*- coding: utf-8 -*-
from django.views.generic import ListView
from ..models import ClinicalTrial

class ClinicalTrialsIndexView(ListView):
    template_name = "ctrials/index.html"
    
    def get_queryset(self):
        """ We want see ClinicalTrial as for desease requested. """
        self.items = ClinicalTrial.objects.all()

            
    def get_context_data(self, **kwargs):
        vdata = super(ClinicalTrialsIndexView, self).get_context_data(**kwargs)
        vdata["items"] = self.items
        return vdata
