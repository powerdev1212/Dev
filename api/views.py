# -*- coding: utf-8 -*-
import json
from django.http import JsonResponse, HttpResponse
from experts.models import Expert

def experts_list_json(request):
    exp = {}
    try:
        experts = Expert.objects.select_related().order_by("id")
        exp["listing"] = []
        for expert in experts:
            attrs = (
                    "id",
                    "inner_name",
                    "first_name",
                    "last_name",
                    "so_agreement",
                    "degrees",
                    "bio",
                    "research_interests",
                    "appointment_id",
                    "location_id",
                    "training_new",
                    "seniority",
                    "phone",
                    "email",
                    "profile_picture",
                    )
            e = {k:unicode(v) or "" for k,v in expert.__dict__.iteritems() if not k.startswith("_")}
            exp["listing"].append(e)
    except:
        pass
    return JsonResponse(exp)


def expert_instance_json(request, expert_id):
    exp = {}
    try:
        expert = Expert.objects.select_related().get(pk=expert_id)
        exp = {}
        e = {k:unicode(v) or "" for k,v in expert.__dict__.iteritems() if not k.startswith("_")}
        exp = e
    except:
        pass
    return JsonResponse(exp)
