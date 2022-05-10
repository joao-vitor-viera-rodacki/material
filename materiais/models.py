from django.db import models
from uuid import uuid4


def  upload_image(intance,filename):
  return f"{intance.id_material}-{filename}"

class materiais(models.Model):
  id_material = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  nome = models.CharField(max_length=100)
  quantidade = models.IntegerField()
  preco = models.IntegerField()
  image = models.ImageField(upload_to=upload_image, blank=True, null=True)
  