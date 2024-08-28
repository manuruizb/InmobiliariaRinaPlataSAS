from django.db import models
from ..Propiedades.models import *
from ..Usuarios.models import *
from ..Empleados.models import Empleados

# Create your models here.

class Facturacion(models.Model):
    
    class Meta:
        verbose_name = "Facturacion"
        verbose_name_plural = "Facturacion"
        
        
    value = models.IntegerField('Valor')
    date = models.DateField('Fecha')
    idPropiedad = models.ForeignKey(Propiedades, on_delete=models.CASCADE, default=0)
    idPropietario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=0)
    idEmpleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, default=0)
    
    
    def __str__(self):
        return f'{self.idPropietario} - {self.value} - {self.date} - {self.idEmpleado}'