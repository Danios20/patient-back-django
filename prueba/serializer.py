from rest_framework import serializers
from prueba.models import Patient
class AdminPatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
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
            "state")
        read_only = ("id", )