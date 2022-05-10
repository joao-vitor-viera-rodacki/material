from operator import mod
from rest_framework import viewsets
from materiais.api import serializers
from materiais import models


class MateriaisViewsets(viewsets.ModelViewSet):
  serializer_class = serializers.MateriaisSerializiers
  queryset = models.materiais.objects.all()




