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


from rest_framework.views import APIView
from experts import serializers, models
from rest_framework.response import Response
# Create your views here.


class ExpertUpdate(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        expert = models.Expert.objects.get(pk=pk)
        data = serializers.Expert(expert)
        return Response(data.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        expert = models.Expert.objects.get(pk=pk)
        d=request.data
        expert.so_agreement = request.data['so_agreement']
        expert.save()
        data = serializers.Expert(expert)
        return Response(data.data)
