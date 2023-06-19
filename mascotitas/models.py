from django.db import models

# Create your models here.

class Especie(models.Model):
    idEspecia = models.IntegerField(primary_key=True, verbose_name="Id de Especie")
    nombreEspecie=models.CharField(max_length=50, blank=True, verbose_name="Nombre de Especie")


    def __str__(self):
        return self.nombreEspecie

class Tamaño(models.Model):
    idTamaño = models.IntegerField(primary_key=True, verbose_name="Id de Tanaño")
    nombreTamaño=models.CharField(max_length=50, blank=True, verbose_name="Nombre de Tamaño")
    
    def __str__(self):
        return self.nombreTamaño


class Animal(models.Model):
    nombre=models.CharField(primary_key=True, max_length=15, verbose_name="Nombre")
    genero=models.CharField(max_length=50, blank=True, verbose_name="Genero")
    imagen=models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    especie=models.ForeignKey(Especie, on_delete=models.CASCADE, verbose_name="Especie")
    tamaño=models.ForeignKey(Tamaño, on_delete=models.CASCADE, verbose_name="Tamaño")
    descripcion=models.CharField(max_length=150, blank=True, verbose_name="Descripcion")


    def __str__(self):
        return self.nombre


