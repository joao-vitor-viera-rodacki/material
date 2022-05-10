from django.db import models

class materiais(models.Model):
  nome = models.CharField(max_length=100)
  quantidade = models.IntegerField()
  preco = models.IntegerField()
  