from rest_framework import serializers
from taxonomy import models
class Vocabulary(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Vocabulary
        fields=('description', 'hierarchy', 'module', 'inner_name')

class Term(serializers.HyperlinkedModelSerializer):
    #vocab = Vocabulary()
    class Meta:
        model = models.Term
        fields =(#'vocab',
        'description', 'weight', 'inner_name')
