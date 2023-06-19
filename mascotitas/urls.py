from django.urls import path
from .views import Inicio, dos,crear, accesperro,eliminar,modificar, accesgato, adoptar, mision, registrar, vet  , adoptar, crear

urlpatterns = [
    path('', Inicio, name="Inicio"),
    path('accesperro/', accesperro , name="Acceosrios Perros"),
    path('accesgato/', accesgato , name="Accesorios Gatos"),
    path('mision/', mision , name="Mision"),
    path('registrar/', registrar , name="registrar"),
    path('vet/', vet , name="Veterinarios"),
    path('adoptar/', adoptar , name="Adoptar"),
    path('crear/', crear , name="Crear"),
    path('dos/', dos , name="dos"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('crear/', crear, name="crear"),
]
