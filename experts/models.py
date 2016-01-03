# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

from assets import models as am


class ExpertInstitutionManager(models.Manager):
    """ Manager for expert institution model """
    def get_actives(self):
        try:
            #return ExpertInstitutionManager.all()
            return super(ExpertInstitutionManager, self).get_queryset()\
            .filter(active=True)\
            .order_by("inner_name")
        except:
            return False
        
class ExpertInstitution(am.AbstractRankedAPIFeatured):
    """ Expert institution data model. """
    class Meta:
        verbose_name = "institution"
        verbose_name_plural = "institutions"
    old_id = models.IntegerField(blank=True, null=True)
    old_expert_id = models.IntegerField(blank=True, null=True)
    experts = models.ManyToManyField("Expert",
                                     related_name="institutions",
                                     verbose_name="Experts in this institution"
                                     )
    objects = models.Manager()
    mgr = ExpertInstitutionManager()
    
    def __unicode__(self):
        return "{0} ({1})".decode("UTF-8").format(self.inner_name,str(self.id))
    
    def assigned_to(self):
        return self.experts.count()
    assigned_to.short_description = "Experts assigned"


class ExpertDepartment(am.AbstractRankedAPIFeatured):
    """ Expert department data model. """
    class Meta:
        verbose_name = "department"
        verbose_name_plural = "departments"
    institution = models.ForeignKey(ExpertInstitution,
        blank=True,
        null=True,
        verbose_name="Expert`s institution",
        related_name="departments"
        )


class ExpertAppointment(am.AbstractRankedAPIFeatured):
    old_expert_id = models.IntegerField("old_expert_id", blank=True, null=True)
    department = models.ForeignKey(ExpertDepartment,
                                   blank=True, null=True,
                                   verbose_name="expert`s department",
                                   related_name="experts")
    def show_owner(self):
        try:
            return Expert.objects.get(old_id=self.old_expert_id).inner_name
        except:
            return "No expert found"
    show_owner.short_description = "Owner"

    class Meta:
        verbose_name = "expert appointment"
        verbose_name_plural = "expert appointments"


class ExpertEducation(am.AbstractStandardAPIFeatured):
    old_expert_id = models.IntegerField("old_expert_id", blank=True, null=True)

    class Meta:
        verbose_name = "expert education"
        verbose_name_plural = "expert educations"
        
        
class ExpertLocation(am.AbstractStandardAPIFeatured):
    old_expert_id = models.IntegerField("old_expert_id", blank=True, null=True)

    class Meta:
        verbose_name = "expert location"
        verbose_name_plural = "expert locations"


class ExpertTraining(am.AbstractStandardAPIFeatured):
    old_expert_id = models.IntegerField("old_expert_id", blank=True, null=True)

    class Meta:
        verbose_name = "expert training"
        verbose_name_plural = "expert trainings"


class ExpertBoardSertification(am.AbstractStandardAPIFeatured):
    old_expert_id = models.IntegerField("old_expert_id", blank=True, null=True)

    class Meta:
        verbose_name = "expert sertification"
        verbose_name_plural = "expert sertifications"
        
class ExpertExperience(am.AbstractStandardAPIFeatured):
    old_expert_id = models.IntegerField("old_expert_id", blank=True, null=True)

    class Meta:
        verbose_name = "expert`s experience"
        verbose_name_plural = "experts` experience"
        
class ExpertAward(am.AbstractStandardAPIFeatured):
    old_expert_id = models.IntegerField("old_expert_id", blank=True, null=True)

    class Meta:
        verbose_name = "expert`s award"
        verbose_name_plural = "experts` awards"


class Expert(am.AbstractRankedAPIFeatured):
    """ Expert data model(start structure, needs to be extended). """
    class Meta:
        verbose_name = "expert"
        verbose_name_plural = "experts"
    old_id = models.IntegerField("old_id", blank=True, null=True)
    first_name = models.CharField("First Name",max_length=150, blank=True)
    last_name = models.CharField("Last Name",max_length=150, blank=True)
    so_agreement = models.BooleanField("SO Argeement",
                                       default=False,
                                       help_text="Agreed to consult",
                                       )
    degrees = models.CharField("Degrees",max_length=150, blank=True)
    bio = models.TextField("Bio Statement", max_length=1000, blank=True, null=True)
    specialities = models.ManyToManyField("taxonomy.Term",
        blank=True,
        verbose_name="Specialities",
        related_name="experts_of_this_speciality",
        )
    clinical_expertises = models.ManyToManyField("taxonomy.Term",
        blank=True,
        verbose_name="Clinical Expertises",
        related_name="experts_researching_this"
        )
    research_interests = models.TextField("Research Interests", blank=True)
    appointment = models.ForeignKey(ExpertAppointment,
        related_name="experts_appointed",
        verbose_name="Appointment",
        blank=True,
        null=True)
    location = models.ForeignKey(ExpertLocation,
        related_name="experts_located",
        verbose_name="Location",
        blank=True,
        null=True
        )
    # expert can have one or more educations
    medical_educations = \
        models.ManyToManyField(ExpertEducation,
                               related_name="experts_has_such_education",
                               verbose_name="Medical Education",
                               blank=True)
    training_new = models.TextField("Trainings", blank=True, null=True)
    # expert might be trained one or more times
    trainings = models.ManyToManyField(ExpertTraining,
                                       related_name="experts_trained",
                                       verbose_name="Trainings",
                                       blank=True)
    # expert could be sertified in one or more sertifications
    board_certifications = \
        models.ManyToManyField(ExpertBoardSertification,
                               blank=True,
                               related_name="experts_sertified",
                               verbose_name="Board Certifications")
    experiences = models.ManyToManyField(ExpertExperience, blank=True,
                                         related_name="Experience",
                                         verbose_name="Experience")
    awards = models.ManyToManyField(ExpertAward, blank=True,
                                    related_name="experts_awarded",
                                    verbose_name="Honors and Awards")
    seniority = models.IntegerField("Seniority", default=0)
    phone = models.CharField("Phone", max_length=150, blank=True)
    email = models.EmailField("Email", max_length=150, blank=True)
    profile_picture = models.ImageField("", upload_to="images/experts",
                                        blank=True, null=True)
    
    def institution_rank(self):
        """ Shows rank for expert`s institution. """
        try:
            return self.appointment.department.institution.rank
        except:
            return "No rank for the institution."
    institution_rank.short_description = "Inst. rank"

    def institution(self):
        """ Shows name of expert`s institution. """
        try:
            return self.appointment.department.institution.inner_name
        except:
            return "No expert`s institution name."
    institution.short_description = "Inst. name"

    def owns_clinical_expertises(self):
        expertises = [i.inner_name for i in self.clinical_expertises.all()]
        return ", ".join(expertises) or "No expertises"
    owns_clinical_expertises.short_description = "Cl.expertises"
    
    @property
    def get_experiences(self):
        return self.experiences.all()

