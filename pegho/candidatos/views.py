from django.shortcuts import render
from rest_framework import viewsets
from .models import DadosPessoais
from .serializers import DadosPessoaisSerializer

class DadosPessoaisViewSet(viewsets.ModelViewSet):
    queryset = DadosPessoais.objects.all()
    serializer_class = DadosPessoaisSerializer

