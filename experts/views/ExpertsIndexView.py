# -*- coding: utf-8 -*-
from django.views.generic import ListView
from ..models import Expert

class ExpertsIndexView(ListView):
    template_name = "experts/index.html"
    
    def get_queryset(self):
        # get item by categories set
        self.ditem = DeseaseItem.mgr\
        .get_by_categories_set([i for i in self.kwargs.itervalues()])
    
    def get_context_data(self, **kwargs):
        vdata = super(ExpertsIndexView, self).get_context_data(**kwargs)
        vdata["ditem"] = self.ditem
        vdata["experts"] = self.ditem.get_experts()
        return vdata
