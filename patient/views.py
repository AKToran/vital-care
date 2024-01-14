from rest_framework import viewsets
from rest_framework.views import APIView
from .import models
from . serializers import PatientSerializer, RegistrationSerializer
from rest_framework.response import Response

class PatientViewset(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = PatientSerializer

class RegistrationApiView(APIView): 
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response('Registration successful')
        
        return Response(serializer.errors)

