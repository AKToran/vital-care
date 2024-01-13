from django.shortcuts import render
from rest_framework import viewsets
from .import models
from . serializers import SeviceSerializer

class ServiceViewset(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = SeviceSerializer
