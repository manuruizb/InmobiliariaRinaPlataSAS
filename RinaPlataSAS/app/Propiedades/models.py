from django.db import models
from ..Usuarios.models import *
from ..Empleados.models import *

# Create your models here.

class Propiedades(models.Model):

    class Meta:
        verbose_name = "Propiedades"
        verbose_name_plural = "Propiedades"

    tipoDePropiedad = models.CharField('Tipo De Propiedad', max_length=100)
    valor = models.IntegerField('Valor')
    direccion = models.CharField('Direccion', max_length=100)
    idPropetario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=0)
    status = models.BooleanField('Estado', default=False)
    idEmpleado = models.ForeignKey(Empleados, on_delete=models.CASCADE, default=0)


    def __str__(self):
        return f'{self.tipoDePropiedad} - {self.valor} - {self.status}'
