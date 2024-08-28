from rest_framework import serializers
from .models import *

class FacturacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Facturacion
        fields = ('__all__')