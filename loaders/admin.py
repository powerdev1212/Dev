# -*- coding: utf-8 -*-

from django.contrib import admin
from . import models
from assets import models as am
from . import handlers as leh

class LoaderEngineConfigInline(admin.StackedInline):
    model = models.LoaderEngineConfig
    extra = 1


class LoaderEngineSelectorInline(admin.TabularInline):
    model = models.LoaderEngineSelector
    extra = 0


class LoaderEngineAdmin(am.APIFeaturedModelAdmin):
    inlines = [LoaderEngineConfigInline, LoaderEngineSelectorInline]
admin.site.register(models.LoaderEngine, LoaderEngineAdmin)


class ExpertsLoadedStorageAdmin(admin.ModelAdmin):
    actions = ["start_asco_load_engine", "start_hopkins_load_engine"]
    list_display = ["__str__", "first_name", "last_name", "phone", "active"]
    search_fields = ("inner_name", "first_name", "last_name")
    list_filter = ("country",)
    
    def start_asco_load_engine(self, request, queryset):
        """ Load data from asco.org """
        engine = models.LoaderEngine.objects.get(mnemo="asco", active=True)
        handler = leh.ASCOUploadHandler(engine, **{k: v for k, v in engine.config.__dict__.iteritems()})
        handler.process()
    start_asco_load_engine.short_description = """
    Load experts data from asco.org
    """

    def start_hopkins_load_engine(self, request, queryset=[]):
        """ Load data from hopkinsmedicine.org """
        engine = models.LoaderEngine.objects.get(mnemo="hopkinsmedicine", active=True)
        handler = leh.HopkinsMedicineUploadHandler(engine,
            **{k: v for k, v in engine.config.__dict__.iteritems()})
        handler.process()
    start_hopkins_load_engine.short_description="Load experts data from hopkinsmedicine.org"
        
admin.site.register(models.ExpertsLoadedStorage, ExpertsLoadedStorageAdmin)


class CancerStudyLoadedStorageAdmin(admin.ModelAdmin):
    actions = ["load_from_cbioportal"]
    list_display = ("__str__","active")
    search_fields = ("inner_name",)
    
    def load_from_cbioportal(self, request, queryset):
        engine = models.LoaderEngine.objects.get(mnemo="cbioportal", active=True)
        handler = leh.CBioUploadHandler(**{k: v for k, v in engine.config.__dict__.iteritems()})
        handler.process()
        #raise Exception(handler._data)
    load_from_cbioportal.short_description = "Load cancer types from www.cbioportal.org"
admin.site.register(models.CancerStudyLoadedStorage, CancerStudyLoadedStorageAdmin)
