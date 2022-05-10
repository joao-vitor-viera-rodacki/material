from atexit import register
from django.contrib import admin
from materiais import models
 

admin.site.register(models.materiais)