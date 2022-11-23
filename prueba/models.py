from django.db import models

# Create your models here.
class Patient(models.Model):
    patient = models.CharField(max_length=100, null=False, blank=False)
    documentType = models.CharField(max_length=100, null=False, blank=False)
    document = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100, null=False, blank=False)
    dentist = models.CharField(max_length=100, null=False, blank=False)
    bloodType = models.CharField(max_length=100, null=False, blank=False)
    treatment = models.CharField(max_length=100, null=False, blank=False)
    price = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=100, null=False, blank=False)

    class Meta: db_table = "patients"
