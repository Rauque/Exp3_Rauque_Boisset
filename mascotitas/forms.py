from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tamaño, Especie, Animal 


class RegistroUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre','genero', 'imagen','especie','tamaño','descripcion']
        labels = {
            'nombre': 'Nombre',
            'genero': 'Genero',
            'imagen': 'Imagen',
            'especie':'Especie',
            'tamaño':'Tamaño',
            'descripcion': 'Descripcion'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese nombre del animal..',
                    'id': 'nombre',
                }
            ),
            'genero':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese genero..',
                    'id': 'genero',
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'id': 'imagen',
                    'class': 'form-control',
                }
            ),
            'especie': forms.Select (
                attrs={
                    'class': 'form-control',
                    'id':'especie',
                }
            ),
            'tamaño': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id':'tamaño',
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descripcion..',
                    'id': 'descripcion',
                }
            )

        }