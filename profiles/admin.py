# -*- coding: utf-8 -*-

from django.contrib import admin
from . import models



class MainUserAdmin(admin.ModelAdmin):
    pass
admin.site.register(models.MainUser, MainUserAdmin)
