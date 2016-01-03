# -*- coding: utf-8 -*-
import requests
from django.http import Http404
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from hygeiais.settings import PARTNER_PAGE_URL
from deseases.models import DeseaseItem
from experts.models import ExpertInstitution, Expert
from loaders.models import LoaderEngine
from loaders.handlers import PublicationsUploadHandler
from taxonomy.models import Term


class DeseaseItemView(ListView):

    template_name = "deseases/item.html"
    pub_loader = PublicationsUploadHandler

    def get_queryset(self):
        # get item by categories set
        self.ditem = DeseaseItem.mgr\
        .get_by_categories_set([i for i in self.kwargs.itervalues()])

    def get_guide(self, guideline):
        g = {}
        g["ident"] = guideline.id
        g["link"] = True if guideline.link!="" else False
        g["treatment"] = guideline.treatment.inner_name
        g["issuer"] = guideline.issuer.inner_name.lower()
        g["data"] = guideline.process_data()
        return g

    def get_nci_guidelines(self):
        guides = []
        excluded_ids = []
        def _get_nci_guidelines(node, stack, excluded_ids):
            excluded_ids = [i["ident"] for i in stack]
            for treatment in node.treatments.all():
                for guideline in treatment.guidelines\
                .filter(issuer__inner_name__iexact="nci", active=True)\
                .exclude(pk__in=excluded_ids):
                    stack.append(self.get_guide(guideline))
            if not stack:
                if node.parent:
                    _get_nci_guidelines(node.parent, stack, excluded_ids)
        _get_nci_guidelines(self.ditem, guides, excluded_ids)
        return guides

    def get_nccn_guidelines(self):
        guides = []
        for treatment in self.ditem.treatments.all():
            for guideline in treatment.guidelines.filter(issuer__inner_name__iexact="nccn", active=True):
                #guides.append(guideline.process_data())
                guides.append(self.get_guide(guideline))
        return guides

    def get_experts(self):
        """ Get experts paginated """
        kw = {}
        field_institution_tid = self.request.GET.get("field_institution_tid", False)
        field_speciality_tid = self.request.GET.get("field_speciality_tid", False)
        try:
            field_institution_tid = int(field_institution_tid)
            kw.update(institutions__id__in=[field_institution_tid])
        except:
            pass
        try:
            field_speciality_tid = int(field_speciality_tid)
            kw.update(specialities__id__in=[field_speciality_tid])
        except:
            pass
        #raise Exception(kw)
        experts = self.ditem.get_experts(**kw)
        self.experts = experts
        #self.paginator = Paginator(self.experts, 20)
        #self.page = self.request.GET.get("p")
        #experts = self.experts[:]
        #try:
        #    experts = self.paginator.page(self.page)
        #except PageNotAnInteger:
        #    experts = self.paginator.page(1)
        #except EmptyPage:
        #    experts = self.paginator(self.paginator.num_pages)
        return self.experts

    def get_institutions(self):
        """ Get all institutions """
        self.institutions = ExpertInstitution.mgr.get_actives()
        return self.institutions

    def get_specialities(self):
        """ Get all specialities """
        specialities = []
        #experts = Expert.objects.all()
        experts = self.get_experts()
        for expert in experts:
            specialities.extend([i.id for i in expert.specialities.filter(active=True)])
        specialities = set(tuple(specialities))
        self.specialities = Term.objects\
            .filter(id__in=specialities)\
            .order_by("inner_name")
        return self.specialities

    def get_publications(self):
        """ Get all publications from remote site """
        engine = LoaderEngine.objects.get(mnemo="publications", active=True)
        self.handler = self.pub_loader(engine, **{k: v for k, v in engine.config.__dict__.iteritems()})
        search_values=[]
        # item name
        self.handler.search_values.append(self.ditem.inner_name.replace(" ", "+"))
        # parent item name
        try:
            self.handler.search_values.append(self.ditem.parent.inner_name.replace(" ", "+"))
        except:
            pass
        # full request string
        self.handler.search_values = ["+AND+".join(self.handler.search_values)]
        self.handler.process()
        return self.handler._documents or False

    def get_hs_info(self):
        """ Get information for health specialist """
        hs_info = []

        # detailed definition
        try:
            hs_detailed_definition = {
                "name": "Detailed definition",
                "data": self.ditem.detailed_definition,
                "mnemo": "detailed_definition",
            }
        except:
            hs_detailed_definition = None
        hs_info.append(hs_detailed_definition)

        # epidemiology
        try:
            hs_epidemiology = {
                "name": "Epidemiology",
                "data": self.ditem.epidemiology,
                "mnemo": "epidemiology",
            }
        except:
            hs_epidemiology = None
        hs_info.append(hs_epidemiology)

        # clinical features
        try:
            hs_clinical_features = {
                "name": "Clinical features",
                "data": self.ditem.clinical_features,
                "mnemo": "clinical_features",
            }
        except:
            hs_clinical_features = None
        hs_info.append(hs_clinical_features)

        # etiology
        try:
            hs_aetiology = {
                "name": "Aetiology",
                "data": self.ditem.etiology,
                "mnemo": "etiology",
            }
        except:
            hs_aetiology = None
        hs_info.append(hs_aetiology)

        # histopathology
        try:
            hs_histopathology = {
                "name": "Histopathlogy",
                "data": self.ditem.histopathology,
                "mnemo": "histopathology",
            }
        except:
            hs_histopathology = None
        hs_info.append(hs_histopathology)

        # genetics
        try:
            hs_genetics = {
                "name": "Genetics",
                "data": self.ditem.genetics,
                "mnemo": "genetics",
            }
        except:
            hs_genetics = None
        hs_info.append(hs_genetics)

        # prognostic factors
        try:
            hs_pgfactors = {
                "name": "Prognostic factors",
                "data": self.ditem.prognostic_factors,
                "mnemo": "prognostic_factors",
            }
        except:
            hs_pgfactors = None
        hs_info.append(hs_pgfactors)

        return hs_info

    def get_patient_info(self):
        """ Get information for patients """
        patient_info = []
        try:
            patient_version = {
                "name": "For patients",
                "data": self.ditem.patient_version,
                "mnemo": "patient_version",
            }
        except:
            patient_version = None
        patient_info.append(patient_version)
        return patient_info

    def get_genomic_studies(self):
        """ Get genomic data """
        try:
            return self.ditem.genomic_studies.filter(active=True).order_by("id")
        except:
            return False

    def get_context_data(self, **kwargs):
                vdata = super(DeseaseItemView, self).get_context_data(**kwargs)
                vdata["ditem"] = self.ditem

                """
                Type of data in details depends on user permissions type.
                If user is in 'Health specialist' group he can view detailed view
                for each desease as a specialist.
                Another way if user is in 'Patient' group he can view patient_version
                of information.
                Unregistered user can view patient_version(right way?).
                """
                if self.request.user.is_authenticated():
                    if self.request.user.has_perm("deseases.can_view_hs_info") or \
                    self.request.user.is_expert or self.request.user.is_physician:
                        vdata["pagetitle"] = "Health specialist info"
                        vdata["details"] = self.get_hs_info()
                    elif self.request.user.has_perm("deseases.can_view_patient_info"):
                        vdata["pagetitle"] = "Patient info"
                        vdata["details"] = self.get_patient_info()
                    else:
                        vdata["pagetitle"] = "Details"
                        vdata["details"] = self.get_patient_info()
                else:
                    vdata["pagetitle"] = "Details"
                    vdata["details"] = self.get_patient_info()

                vdata["partner_page_url"] = PARTNER_PAGE_URL
                vdata["experts"] = self.get_experts() if "experts" in self.request.GET else False
                vdata["institutions"] = self.get_institutions() if "experts" in self.request.GET else False
                vdata["specialities"] = self.get_specialities() if "experts" in self.request.GET else False
                vdata["guidelines"] = {
                    "nci": self.get_nci_guidelines(),
                    "nccn": self.get_nccn_guidelines(),
                    } if "treatment" in self.request.GET else False
                vdata["publications"] = self.get_publications() if "publications" in self.request.GET else False
                vdata["related_cancers"] = self.ditem.get_related_items()
                vdata["support_groups"] = self.ditem.get_support_groups()
                vdata["genomic_studies"] = self.get_genomic_studies() if "genomic-studies" in self.request.GET else False
                return vdata
