
from rest_framework import serializers 
from materiais import models

class MateriaisSerializiers(serializers.ModelSerializer):
  class Meta:
    model = models.materiais
    fields = '__all__'