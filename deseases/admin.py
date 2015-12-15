# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models
from ctrials import models as ctrm
from discussions import models as dscm
from publications import models as pubm
from assets import models as am

###############################################################################


class PatientVersionUrlInline(admin.TabularInline):
    model = models.PatientVersionUrl
    extra = 0


class PatientVersionImageInline(admin.TabularInline):
    model = models.PatientVersionImage
    extra = 0


class DeseaseImageInline(admin.TabularInline):
    model = models.DeseaseImage
    extra = 0


class ClinicalTrialImageInline(admin.TabularInline):
    model = ctrm.ClinicalTrialImage
    extra = 0


class DiscussionImageInline(admin.TabularInline):
    model = dscm.DiscussionImage
    extra = 0


class PublicationImageInline(admin.TabularInline):
    model = pubm.PublicationImage
    extra = 0


class PublicationTweetImageInline(admin.TabularInline):
    model = pubm.PublicationTweetImage
    extra = 0
###############################################################################


class DeseasesTypeAdmin(am.APIFeaturedModelAdmin):
    pass
admin.site.register(models.DeseaseType, DeseasesTypeAdmin)

"""
class DeseaseCategoryAdmin(am.APIFeaturedModelAdmin):
    list_display = ("__str__", "rank", "active")
    ordering = ("rank",)
    inlines = (
        PatientVersionUrlInline,
        PatientVersionImageInline,
        DeseaseImageInline,
        ClinicalTrialImageInline,
        DiscussionImageInline,
        PublicationImageInline,
        PublicationTweetImageInline,
        )
admin.site.register(models.DeseaseCategory, DeseaseCategoryAdmin)
"""


class DeseaseItemAdmin(am.APIFeaturedModelAdmin):
    list_display = ("__str__", "old_id", "parent", "has_synonyms",
                   "has_taxonomy_terms", "count_experts", "rank", "active")
    ordering = "inner_name",
    search_fields = "inner_name", "old_id", "old_parent"
    inlines = (
        PatientVersionUrlInline,
        PatientVersionImageInline,
        DeseaseImageInline,
        ClinicalTrialImageInline,
        DiscussionImageInline,
        PublicationImageInline,
        PublicationTweetImageInline,
        )
admin.site.register(models.DeseaseItem, DeseaseItemAdmin)
