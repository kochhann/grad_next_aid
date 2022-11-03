from django.db import models
from apps.core.models import Base
from apps.routine.models import Medication


class History(Base):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    history_date = models.DateField('Data histórico', blank=False, null=False)
    medication = models.ForeignKey(Medication, verbose_name='Medicação', on_delete=models.PROTECT, blank=False, null=False)
    quantity_in = models.IntegerField('Entrada', blank=False, null=False, default=0)
    quantity_out = models.IntegerField('Saída', blank=False, null=False, default=0)

    def __str__(self):
        return f'Histórico de {self.medication.name} para {self.history_date}'

    class Meta:
        verbose_name = 'Histórico'
        verbose_name_plural = 'Históricos'


class Prognostic(Base):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    medication = models.ForeignKey(Medication, verbose_name='Medicação', on_delete=models.PROTECT, blank=False,
                                   null=False)
    prognostic_date = models.DateField('Data prognóstico', blank=False, null=False)
    quantity_in = models.IntegerField('Entrada', blank=False, null=False, default=0)
    quantity_out = models.IntegerField('Saída', blank=False, null=False, default=0)

    def __str__(self):
        return f'Previsão de {self.medication.name} para {self.history_date}'

    class Meta:
        verbose_name = 'Prognóstico'
        verbose_name_plural = 'Prognósticos'

