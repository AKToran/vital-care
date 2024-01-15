from django.shortcuts import render
from rest_framework import viewsets
from .import models
from . serializers import SeviceSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ServiceViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Service.objects.all()
    serializer_class = SeviceSerializer
