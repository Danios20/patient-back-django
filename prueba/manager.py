from prueba.models import Patient
from prueba.serializer import AdminPatientsSerializer
class AdminPatientsManager():
    @staticmethod
    def get_all(offset, limit):
        patients = Patient.objects.all()[limit:offset]
        serializer = AdminPatientsSerializer(patients, many=True)
        return serializer.data

    @staticmethod
    def save_patient(serializer):
        try:
            patient = serializer.save()
        except Exception as e:
            raise

    @staticmethod
    def get_patient_by_id(pk):
        try:
             patient = Patient.objects.get(pk = pk)
             serializer = AdminPatientsSerializer(patient, many=False)
             return serializer.data
        except Exception as e:
            raise

    @staticmethod
    def update_patient(data, pk):
        try:
             patient_old = Patient.objects.get(pk = pk)
             serializer = AdminPatientsSerializer(patient_old,data=data)
             if serializer.is_valid(raise_exception=True):
                 serializer.save()
        except Exception as e:
            raise

    @staticmethod
    def delete_patient(pk):
        try:
             patient = Patient.objects.get(pk = pk)
             patient.delete()
        except Exception as e:
            raise
