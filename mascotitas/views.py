from django.shortcuts import render, redirect
from .models import *
from .forms import RegistroUserForm, AnimalForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


def Inicio(request):
    return render(request, 'Inicio.html')

@login_required
def dos(request):
    mascotitas = Animal.objects.raw('Select * from mascotitas_animal')
    datos ={'animalito':mascotitas}
    return render(request, 'dos.html', datos)

def accesperro(request):
    return render(request, 'Acceosrios Perros.html')

def accesgato(request):
    return render(request, 'Accesorios Gatos.html')

def mision(request):
    return render(request, 'Mision.html')

def registro(request):
    return render(request, 'registro.html')

def vet(request):
    return render(request, 'Veterinarios.html')

def adoptar(request):
    return render(request, 'Adoptar.html')

def crear(request):
    return render(request, 'Crear Info.html')


@login_required
def crear(request):
    if request.method=='POST':
        animalform = AnimalForm(request.POST, request.FILES)
        if animalform.is_valid():
            animalform.save()     #similar al insert en función
            return redirect('dos')
    else:
        animalform=AnimalForm()
    return render(request, 'Crear Info.html',{'animalform': animalform})

@login_required
def eliminar(request, id):
    animalEliminado=Animal.objects.get(nombre=id)  #obtenemos un objeto por su pk
    animalEliminado.delete()
    return redirect('dos')

@login_required
def modificar(request,id):
    animal = Animal.objects.get(nombre=id)         #obtenemos un objeto por su pk
    datos ={
        'form':AnimalForm(instance=animal)
    }
    if request.method=='POST':
        formulario = AnimalForm(data=request.POST, instance=animal)
        if formulario.is_valid:
            formulario.save()
            return redirect ('dos')
    return render(request, 'modificar.html', datos)





#método que permite registrar un usuario
def registrar(request):
    data = {
        'form' : RegistroUserForm()         #creamos un objeto de tipo forms para user
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data = request.POST)  
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"],
                  password=formulario.cleaned_data["password1"])
            login(request,user)   
            return redirect('Inicio')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)


def adoptar(request):
    animalito = Animal.objects.all()
    datos={
        'animalito': animalito
    }
    return render(request,'Adoptar.html',datos)