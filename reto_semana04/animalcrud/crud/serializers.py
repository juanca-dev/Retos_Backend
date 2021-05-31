from rest_framework import serializers
from .models import AnimalModel

class MostrarAnimalesSerializer(serializers.ModelSerializer):
  class Meta:
    model = AnimalModel
    fields = '__all__'