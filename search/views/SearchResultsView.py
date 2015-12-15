# -*- coding: utf-8 -*-
from django.db.models import Q
from django.views.generic import ListView
from deseases.models import DeseaseItem
from experts.models import Expert

class SearchResultsView(ListView):

    template_name = "search/index.html"
    trg = None
    outp = []
    
    def prepared_search_phrase(self, phrase):
        """ Prepare fulltext search request. """
        self.phr = None
        phr = []
        # + condition
        phrase_splitted = phrase.split(" ")
        for i in phrase_splitted:
            phr.append(i)
            #phr.append("{0}.*".format(i))
        #raise Exception(phr)
        return "+".join(phr)
        
    def prepare_search_phrase(self, phrase):
        phrase_splitted = [i for i in phrase.split(" ") if len(i) > 2]
        self.phr = phrase_splitted
            
    def get_deseases(self, outp):
        for i in self.phr:
            try:
                deseases = DeseaseItem.objects\
                .filter(
                    Q(inner_name__istartswith=i)
                    )
                for d in deseases:
                    self._set_to_output(**{
                                            "inner_name": d.inner_name,
                                            "path": d.get_path(),
                                            "descr": d.definition,
                                            "bcrs":d.get_bcrs(),
                                        })
            except:
                pass

    def get_queryset(self):
        self.outp = []
        if self.request.GET.get("_trg", False):
            self.prepare_search_phrase(self.request.GET.get("_trg", False))
            self.get_deseases(self.outp)
        # get item by categories set
        '''
        if self.request.GET.get("trg", False):
            try:
                self.deseases = DeseaseItem.objects\
                    .filter(
                        Q(inner_name__startswith=self.prepared_search_phrase(self.request.GET["trg"]))|
                        Q(inner_name__contains=)
                    )
                    #.filter(inner_name__search=self.prepared_search_phrase(self.request.GET["trg"]))
                for d in self.deseases:
                    self.prepare_output(**{
                                          "inner_name": d.inner_name,
                                          "path": d.get_path(),
                                          "descr": d.definition,
                                          "bcrs":d.get_bcrs(),
                                        })
            except:
                pass
            try:
                self.experts = Expert.objects\
                    .filter(inner_name__search=self.prepared_search_phrase(self.request.GET["trg"]))
                for e in self.experts:
                   self.prepare_output(**{
                                          "inner_name": e.inner_name,
                                          "path": None,
                                          "descr": ", ".join([i.inner_name for i in e.specialities.all()]),
                                          "bcrs": None,
                                        })
            except:
                pass
        '''
                
    def _set_to_output(self, **kw):
        self.outp.append(kw)

    def get_context_data(self, **kwargs):
        vdata = super(SearchResultsView, self).get_context_data(**kwargs)
        vdata["referer"] = self.request.META.get("HTTP_REFERER", False) or self.request.path
        vdata["trg"] = self.outp
        return vdata
