from django.db import models
from django.utils import timezone


class Base(models.Model):
    date_created = models.DateField('Criação', auto_now_add=True)
    date_edited = models.DateField('Modificação', auto_now=True)
    date_deactivated = models.DateField('Desativado', blank=True, null=True, default=None)
    active = models.BooleanField('Ativo', default=True)

    def soft_delete(self):
        self.active = False
        self.date_deactivated = timezone.now()
        self.save()

    class Meta:
        abstract = True


class Company(Base):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    cnpj = models.IntegerField('CNPJ', blank=False, null=False)
    name = models.CharField('Razão Social', max_length=500, blank=False, null=False)
    nickname = models.CharField('Nome Fantasia', max_length=200, blank=False, null=False)
    city = models.CharField('Cidade', max_length=200, blank=False, null=False)
    state = models.CharField('Estado', max_length=2, blank=False, null=False)
    address = models.BooleanField('Endereço', default=False)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitais'
