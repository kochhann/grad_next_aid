from django.contrib import admin
from .models import (
    Service,
    Unity,
    Pharmacy,
    MedicationType,
    Medication,
    Reviewer,
    Inventory
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'company']


@admin.register(Unity)
class UnityAdmin(admin.ModelAdmin):
    list_display = ['name', 'service']


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ['name', 'unity']


@admin.register(MedicationType)
class MedicationTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']
    list_filter = ['type']


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['medication', 'quantity']
    list_filter = ['pharmacy']


@admin.register(Reviewer)
class ReviewerAdmin(admin.ModelAdmin):
    list_display = ['user']

