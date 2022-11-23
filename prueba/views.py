from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from prueba.controller import AdminPatientsController
# Create your views here.
class AdminPatientsView(APIView):
    def get(self, request):
        try:
            patient = AdminPatientsController.get_all()
            return Response(patient)
        except Exception as e:
            return Response({'mensaje': f'Ha ocurrido un error {e}'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, format=None):
        try:
            patient = AdminPatientsController.save_patient(request.data)
            if hasattr(patient, "errors") and persona.errors:
                return Response(patient.errors, status = status.HTTP_400_BAD_REQUEST)
            return Response(patient.data, status = status.HTTP_201_CREATED)
        except Exception as e:
             return Response({'mensaje': f'Ha ocurrido un error {e}'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

class AdminPatientsViewDetail(APIView):
    def get(self, request, pk):
        try:
            patient = AdminPatientsController.get_patient_by_id(pk)
            return Response(patient)
        except Exception as e:
            return Response({'mensaje': f'Ha ocurrido un error {e}'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)


    def put(self, request, pk):
        try:
            patient = AdminPatientsController.update_patient(request.data, pk)
            if hasattr(patient, "errors") and patient.errors:
                return Response(patient.errors, status = status.HTTP_400_BAD_REQUEST)
            return Response(data = {'mensaje':'El pacientes ha sido actualizado correctamente'}, status = status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'mensaje': f'Ha ocurrido un error {e}'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            AdminPatientsController.delete_patient(pk)
            return Response(data={'mensaje': 'El paciente ha sido eliminado correctamente'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'mensaje': f'Ha ocurrido un erro {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)