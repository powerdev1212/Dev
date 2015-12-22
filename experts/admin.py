# -*- coding: utf-8 -*-

from django.contrib import admin
from rest_framework.authtoken.models import Token

# -*- coding: utf-8 -*-
from django.forms import ModelForm
from . import models
from assets import models as am

class ExpertForm(ModelForm):
    class Meta:
        model = models.Expert
        fields = (
            "old_id",
            "first_name",
            "last_name",
            "so_agreement",
            "degrees",
            "bio",
            "specialities",
            "clinical_expertises",
            "research_interests",
            "appointment",
            "location",
            "medical_educations",
            "training_new",
            "trainings"
            )

class ExpertInstitutionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "assigned_to", "rank", "active")
    ordering = ("inner_name",)
    search_fields = ("inner_name",)
admin.site.register(models.ExpertInstitution, ExpertInstitutionAdmin)

class ExpertAppointmentAdmin(admin.ModelAdmin):
    list_display = ("__str__","show_owner")
    ordering = ("inner_name",)
    search_fields = ("inner_name",)
admin.site.register(models.ExpertAppointment, ExpertAppointmentAdmin)

class ExpertAdmin(am.APIFeaturedModelAdmin):
    #form = ExpertForm
    list_display = ("__str__","owns_clinical_expertises","active")
    search_fields = ("inner_name", "first_name", "last_name")
    list_filter = "last_name",
    ordering = "last_name",
admin.site.register(models.Expert, ExpertAdmin)

admin.autodiscover()
admin.site.unregister(Token)
