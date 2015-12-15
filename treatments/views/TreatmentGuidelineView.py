# -*- coding: utf-8 -*-
from django.views.generic import ListView
from ..models import TreatmentGuideline

class TreatmentGuidelineView(ListView):
    
    template_name = "treatments/guideline.html"
    
    def get_queryset(self):
        """ We want see categories with no parent only. """
        self.items = TreatmentGuideline.objects.all()

            
    def get_context_data(self, **kwargs):
        vdata = super(TreatmentGuidelineView, self).get_context_data(**kwargs)
        vdata["items"] = self.items
        return vdata
