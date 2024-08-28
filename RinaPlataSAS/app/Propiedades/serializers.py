from rest_framework import serializers
from .models import *

class PropiedadesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Propiedades
        fields = '__all__'