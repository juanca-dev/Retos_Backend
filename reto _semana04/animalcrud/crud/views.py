from .models import AnimalModel
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .serializers import MostrarAnimalesSerializer

class ListarCrearAnimalesController(ListCreateAPIView):
  queryset = AnimalModel.objects.all()
  serializer_class = MostrarAnimalesSerializer

class CRUDAnimalesController(RetrieveUpdateDestroyAPIView):
  queryset = AnimalModel.objects.all()
  serializer_class = MostrarAnimalesSerializer