from django.db import models

# Create your models here.
class Patient(models.Model):
    patient = models.CharField(max_length=100, null=False, blank=False)
    documentType = models.CharField(max_length=100, null=False, blank=False)
    document = models.CharField(max_length=100, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    dentist = models.CharField(max_length=100, null=False, blank=False)
    bloodType = models.CharField(max_length=100, null=False, blank=False)
    treatment = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=12, decimal_places=5, null=False, blank=False)
    state = models.BooleanField(null=False, blank=False, default=1)

    class Meta: db_table = "patients"
