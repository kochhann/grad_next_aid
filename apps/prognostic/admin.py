from django.contrib import admin
from apps.prognostic.models import (
    Prognostic,
    History
)


@admin.register(Prognostic)
class PrognosticAdmin(admin.ModelAdmin):
    list_display = ['medication', 'prognostic_date', 'quantity_in', 'quantity_out']


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['medication', 'history_date', 'quantity_in', 'quantity_out']
