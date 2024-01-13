from rest_framework import serializers
from . import models

class SeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = '__all__'
        