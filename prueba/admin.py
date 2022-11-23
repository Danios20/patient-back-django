from django.contrib import admin
from .models import Patient


# Register your models here.

class AdminPatient(admin.ModelAdmin):
    list_display = [
        "id",
        "patient",
        "documentType",
        "document",
        "email",
        "address",
        "dentist",
        "bloodType",
        "treatment",
        "price",
        "state"]

    list_filter = ["patient", "document", "email"]
    list_editable = ["patient", "document", "email"]
    search_fields = ["document"]
    class Meta:
        models = Patient

admin.site.register(Patient, AdminPatient)