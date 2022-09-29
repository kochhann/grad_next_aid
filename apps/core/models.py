from django.db import models
from django.utils import timezone


class Base(models.Model):
    date_created = models.DateField('Criação', auto_now_add=True)
    date_edited = models.DateField('Modificação', auto_now=True)
    date_deactivated = models.DateField('Desativado', blank=True, null=True, default=None)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True
