from django.db import models
from apps.core.models import Base, Company
from django.contrib.auth.models import User


class Service(Base):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    company = models.ForeignKey(Company, verbose_name='Hospital', on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField('Nome', max_length=200, blank=False, null=False)
    description = models.CharField('Descrição', max_length=1000, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'


class Unity(Base):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    service = models.ForeignKey(Service, verbose_name='Serviço', on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField('Nome', max_length=200, blank=False, null=False)
    description = models.CharField('Descrição', max_length=1000, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'


class Pharmacy(Base):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    unity = models.ForeignKey(Unity, verbose_name='Unidade', on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField('Nome', max_length=200, blank=False, null=False)
    description = models.CharField('Descrição', max_length=1000, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Farmácia'
        verbose_name_plural = 'Farmácias'


class MedicationType(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField('Nome', max_length=200, blank=False, null=False)
    use_range = models.IntegerField('Demanda', blank=False, null=False)
    price_rage = models.DecimalField('Faixa de Preço', max_digits=10, decimal_places=2, null=False, blank=False)
    description = models.CharField('Descrição', max_length=1000, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria de medicamento'
        verbose_name_plural = 'Categorias de medicamento'


class Medication(Base):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    type = models.ForeignKey(MedicationType, verbose_name='Categoria', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField('Nome', max_length=200, blank=False, null=False)
    description = models.CharField('Descrição', max_length=1000, blank=False, null=False)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'


class Inventory(Base):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    pharmacy = models.ForeignKey(Pharmacy, verbose_name='Farmácia', on_delete=models.CASCADE, blank=False, null=False)
    medication = models.ForeignKey(Medication, verbose_name='Medicação', on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.IntegerField('Quantidade', blank=False, null=False, default=0)

    def __str__(self):
        return f'{self.medication.name} - {self.quantity} - {self.date_edited}'

    class Meta:
        verbose_name = 'Estoque'
        verbose_name_plural = 'Estoques'


class Reviewer(Base):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    user = models.ForeignKey(User, verbose_name='Usuário', on_delete=models.PROTECT, blank=False, null=False)
    unity = models.ForeignKey(Unity, verbose_name='Unidade', on_delete=models.PROTECT,
                              blank=False, null=False)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        verbose_name = 'Usuário Revisor'
        verbose_name_plural = 'Usuários Revisores'

