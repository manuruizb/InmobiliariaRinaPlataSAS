from django.db import models


# Create your models here.

class Empleados(models.Model):
    
    class Meta:
        verbose_name = "Empleados"
        verbose_name_plural = "Empleados"
        
    first_name = models.CharField('Nombres', max_length=100)
    lastName = models.CharField('Apellidos', max_length=100)
    idEmpleado = models.CharField('Documento', primary_key=True, max_length=20)
    position_options = (
        ("ASE", "Asesor"),
        ("LIM", "Limpieza"),
        ("ADM", "Administrativo"),
    )
    position = models.CharField('Cargo', max_length=50, blank=False, null=False, choices=position_options, default='ASE')

    def __str__(self):
        return f" {self.first_name} {self.position}"