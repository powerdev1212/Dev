# -*- coding: utf-8 -*-

from django.db import models
from assets import models as am

class LoaderEngine(am.AbstractRankedAPIFeatured):
    
    mnemo = models.CharField("mnemo",
                             max_length=200,
                             blank=True,
                             null=True
                             )

    class Meta:
        verbose_name = "loader engine"
        verbose_name_plural = "loader engines"


class LoaderEngineConfig(am.AbstractStandard):
    """ Configs for loader engines """

    PERIOD_TYPE_CHOICES = (
        ("HO", "Hours"),
        ("DA", "Days"),
        ("WE", "Weeks"),
        ("MO", "Months"),
        )

    DATA_TYPE_CHOICES = (
        ("json", "JSON"),
        ("xml", "XML"),
        ("csv", "CSV"),
        ("text", "TEXT"),
        )

    engine = models.OneToOneField(LoaderEngine,
                               verbose_name="Loader Engine",
                               related_name="config",
                               blank=True,
                               null=True
                               )
    datatype = models.CharField("Type of source data",
                                max_length=10,
                                choices=DATA_TYPE_CHOICES,
                                default=DATA_TYPE_CHOICES[1][0],
                                )
    url = models.TextField("Target site URL",
                           help_text="""
                           Change this value if you exactly 
                           know what you do only:)
                           """
                           )
    url2 = models.TextField("Target site URL(2)",
                           blank=True,
                           null=True,
                           help_text="""
                           Change this value if you exactly 
                           know what you do only:)
                           """
                           )
    search_values = models.TextField("Values for search",
                                     max_length=2000,
                                     blank=True,
                                     null=True,
                                     help_text="""
                                     All values should be 
                                     comma-separated
                                     """
                                     )
    paginator_start = models.IntegerField("Start page",
                                          default=0,
                                          help_text="""
                                          Start page number 
                                          (paginated search)
                                          """
                                          )
    paginator_end = models.IntegerField("Finish page",
                                          default=1,
                                          help_text="""
                                          Finish page number 
                                          (paginated search)
                                          """
                                          )
    period_type = models.CharField("Update Period Type",
                                   max_length=10,
                                   choices=PERIOD_TYPE_CHOICES,
                                   default=PERIOD_TYPE_CHOICES[2][0]   # weekly
                                   )
    value = models.IntegerField("Update Period Value",
                                default=1,   # mean once a week
                                help_text="""
                                Data update will be performed
                                once a 
                                (VALUE) {0} (depends on Update Period Type)
                                """
                                .format(", ".join(i[1] for i in
                                        PERIOD_TYPE_CHOICES))
                                )

    def __unicode__(self):
        return "{0}: {1}".format(self.engine.__unicode__(), "config data")

    class Meta:
        verbose_name = "loader engine config"
        verbose_name_plural = "loader engine configs"


class LoaderEngineSelector(am.AbstractRanked):
    """ Selector expression for Loader Engines """
    engine = models.ForeignKey(LoaderEngine,
                               verbose_name="parent loader engine",
                               related_name="selectors",
                               blank=True,
                               null=True
                               )
    inner_name = models.CharField(max_length=200,
                                  blank=True,
                                  null=True,
                                  help_text="Name of field for usability"
                                  )
    mnemo = models.CharField("mnemo",
                             max_length=200,
                             help_text="Name of field in proper storage"
                             )
    value = models.CharField("expression",
                             max_length=200,
                             help_text="""
                             Selector for retrieve proper 
                             data for the field from source
                             """
                             )
    
    def __unicode__(self):
        return self.inner_name or self.mnemo

    class Meta:
        verbose_name = "selector expression"
        verbose_name_plural = "selector expressions"


class ExpertsLoadedStorage(am.AbstractStandardAPIFeatured):
    """ Temporary storage for loaded experts """
    engine = models.ManyToManyField(LoaderEngine,
                                    blank=True,
                                    related_name="experts_loaded"
                                    )
    first_name = models.CharField("First Name", max_length=150, blank=True)
    last_name = models.CharField("Last Name", max_length=150, blank=True)
    degrees = models.CharField("Degrees", max_length=150, blank=True)
    bio = \
        models.TextField("Bio Statement",
                         max_length=1000,
                         blank=True,
                         null=True)
    specialities = models.TextField("Speciality", blank=True, null=True)
    clinical_expertises = \
        models.TextField("Clinical Expertises", blank=True, null=True)
    research_interests = \
        models.TextField("Research Interests", blank=True, null=True)
    publications = \
        models.TextField("Publications", blank=True, null=True)
    appointment = \
        models.CharField("Appointment", max_length=200, blank=True, null=True)
    # expert can have one or more educations
    medical_educations = \
        models.TextField("Medical Education", blank=True, null=True)
    training_new = models.TextField("Trainings", blank=True, null=True)
    # expert might be trained one or more times
    trainings = models.TextField("Trainings", blank=True, null=True)
    # expert could be sertified in one or more sertifications
    board_certifications = \
        models.TextField("Board Sertifications", blank=True, null=True)
    experiences = models.TextField("Experience", blank=True, null=True)
    awards = models.TextField("Honors & Awards", blank=True, null=True)
    seniority = models.IntegerField("Seniority", default=0)
    country = models.CharField("Country", max_length=150, blank=True)
    state = models.CharField("State", max_length=150, blank=True)
    phone = models.CharField("Phone", max_length=150, blank=True)
    email = models.EmailField("Email", max_length=150, blank=True)
    profile_picture = models.URLField("Expert`s Photo", blank=True, null=True)
    
    def __unicode__(self):
        return "{0}".decode("UTF-8").format(self.inner_name)


    class Meta:
        verbose_name = "loaded expert"
        verbose_name_plural = "loaded experts"


class CancerStudyLoadedStorage(am.AbstractStandardAPIFeatured):
    engine = models.ManyToManyField(LoaderEngine,
                                    blank=True,
                                    related_name="cancerstudies_loaded"
                                    )
    desease = models.ForeignKey("deseases.DeseaseItem",
                                verbose_name="Desease",
                                related_name="genomic_studies",
                                blank=True,
                                null=True
                                )
    mnemo = models.CharField("type_of_cancer_id",
                             max_length=100,
                             blank=True,
                             null=True
                             )
    description = models.TextField("description", blank=True, null=True)
    link = models.URLField("link", blank=True, null=True)
    class Meta:
        verbose_name = "loaded cancer type (www.cbioportal.org)"
        verbose_name_plural = "loaded cancer types (www.cbioportal.org)"
