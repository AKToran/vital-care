from rest_framework import viewsets
from .import models
from . serializers import PatientSerializer

class PatientViewset(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = PatientSerializer
