# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models
from assets import models as am


class PatientAdmin(am.APIFeaturedModelAdmin):
    pass
admin.site.register(models.Patient,PatientAdmin)
