from prueba.manager import AdminPatientsManager
from prueba.serializer import AdminPatientsSerializer
class AdminPatientsController():
    @staticmethod
    def get_all(offset, limit):
        return AdminPatientsManager.get_all(offset, limit)

    @staticmethod
    def save_patient(data):
        serializer = AdminPatientsSerializer(data=data)
        if serializer.is_valid():
            AdminPatientsManager.save_patient(serializer)
            return serializer
        return serializer

    @staticmethod
    def get_patient_by_id(pk):
        return AdminPatientsManager.get_patient_by_id(pk)

    @staticmethod
    def update_patient(data, pk):
        AdminPatientsManager.update_patient(data, pk)

    @staticmethod
    def delete_patient(pk):
        AdminPatientsManager.delete_patient(pk)