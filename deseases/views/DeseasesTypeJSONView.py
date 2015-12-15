# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import JsonResponse
from django.views.generic import ListView
from deseases.models import DeseaseType, DeseaseItem
from assets import views

class DeseasesTypeJSONView(ListView):
    
    template_name = "deseases/type.html"
    default_dtype_mnemo="cancers"
    
    def get_queryset(self):
        """ Get deseases category by mnemo. """
        self.dtype = DeseaseType.mgr\
        .get_by_mnemo(self.kwargs.get("lev0",self.default_dtype_mnemo))
    
    def get_ajax_data(self):
        """ Ajax response. """
        self.get_queryset()
        # get categories of current type
        categories = DeseaseItem.mgr.get_categories_of_dtype(self.dtype)
        # list for data (have category)
        vdata = {
            "name": self.dtype.inner_name,
            "children": [self.set_item_data(category) for category in categories]
        }
        # vdata = [self.set_item_data(category) for category in categories]
        
        # items that have no category except main (desease type)
        #items = DeseaseItem.mgr.get_uncategorized(self.dtype,[c.id for c in categories])
        #vdata_nc = [self.set_item_uncategorized_data(item) for item in items]
        #
        #vdata.extend(vdata_nc)
        return vdata
    
        
    def set_item_data(self, item):
        """ Setting item data. """
        # dict for category data
        children = item.children.filter(active=True)
        return {
        "name": item.inner_name,
        "link": item.get_path(), # get current item children
        "children": [self.set_item_data(ci) for ci in children]
        }
    
    def get(self, request, **kwargs):
        return JsonResponse(self.get_ajax_data(),safe=False)
