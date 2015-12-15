# -*- coding: utf-8 -*-
from .BasicProjectView import BasicProjectView
class DeseasesView(BasicProjectView):
    
    default_dtype_mnemo="cancers"
    
    def get_dtype(self):
        """ Get deseases category by mnemo. """
        self.dtype = DeseaseType.mgr\
        .get_by_mnemo(self.kwargs.get("lev0",self.default_dtype_mnemo))
    
    def get_deseases_list(self):
        self.get_dtype()
        return DeseaseItem.mgr.get_categories_of_dtype(self.dtype)
        
    def get(self, request, **kwargs):
        self.get_dtype()
        self.get_deseases_list()
