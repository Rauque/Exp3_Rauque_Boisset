from django.contrib import admin
from .models import Especie, Tamaño, Animal

# Register your models here.
admin.site.register(Especie)
admin.site.register(Tamaño)
admin.site.register(Animal)

