from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fileds = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'
