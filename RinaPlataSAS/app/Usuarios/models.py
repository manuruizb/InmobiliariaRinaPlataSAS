from django.db import models

# Create your models here.
class Usuario(models.Model):
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuario"
    
    document = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(verbose_name='First Name', max_length=100, blank=False, null=False)
    last_name = models.CharField(verbose_name='Last Name', max_length=100)
    user_types_options = (
    ("PROP", "Propietario"),
    ("ARR", "Arrendatario"),
    )
    user_type = models.CharField(verbose_name='User Type', max_length=30, blank=False, null=False, choices=user_types_options, default='ARR')
    register_date = models.DateField(verbose_name="Date of register", blank=False, null=False)
    
    def __str__(self):
        return f"{self.document} {self.first_name} {self.user_type}"