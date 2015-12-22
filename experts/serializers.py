from rest_framework import serializers
from experts import models
from taxonomy import serializers as taxonomy_serializers


class ExpertDepartment(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ExpertAppointment
        fields=('inner_name', 'institution')


class ExpertAppointment(serializers.HyperlinkedModelSerializer):
    department = ExpertDepartment()
    class Meta:
        model = models.ExpertAppointment
        fields=('inner_name', 'department')


class ExpertExperience(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ExpertExperience
        fields=('inner_name',)


class Expert(serializers.HyperlinkedModelSerializer):
    specialities=taxonomy_serializers.Term(many=True)
    clinical_expertises=taxonomy_serializers.Term(many=True)
    appointment = ExpertAppointment()
    experiences = ExpertExperience(many=True)
    class Meta:
        model = models.Expert
        fields=('pk', 'bio', 'last_name','first_name',
        'so_agreement', 'degrees', 'specialities',

        'clinical_expertises', 'research_interests',
        'appointment',
        # 'medical_educations', 'training_new', 'trainings',
        'experiences',
        #'awards', 'seniority',
        'phone', 'email', 'profile_picture')
