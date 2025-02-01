from django.shortcuts import render
from rest_framework import viewsets
from .models import Ingrediente
from .serializers import IngredienteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer