from django.shortcuts import render
from rest_framework import viewsets
from .models import * 
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *

class PropiedadesViewset(viewsets.ModelViewSet):
    queryset = Propiedades.objects.all()
    serializer_class = PropiedadesSerializers

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fileds = ('__all__')
    search_fields = ('tipoDePropiedad', 'valor', 'direccion', 'status','idPropetario__document', 'idEmpleado__idEmpleado')#('valor', 'tipoDePropiedad')
    ordering_fields = ('__all__')