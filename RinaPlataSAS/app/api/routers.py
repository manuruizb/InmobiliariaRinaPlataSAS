from rest_framework.routers import DefaultRouter
from ..Propiedades.views import *
from ..Usuarios.views import *
from ..Facturacion.views import *
from ..Empleados.views import *

router = DefaultRouter()

router.register(r'Propiedades', PropiedadesViewset, basename='Propiedades')
router.register(r'Usuario', UsuarioViewset, basename='Usuario')
router.register(r'Empleados', EmpleadosViewSet, basename='Empleados')
router.register(r'Facturacion', FacturacionViewSet, basename='Facturacion')

urlpatterns = router.urls