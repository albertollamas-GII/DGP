from turtle import end_fill
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import *
from .funciones import *

def index(request):
    return render(request, 'todoApp/index.html')

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'todoApp/update_task.html', context)

def login(request):
    return render(request, 'todoApp/login.html')

def anadir_menu(request, clase = 'Clase de Ejemplo'):
    profe = obtenerClase(clase)
    
    form = MenuForm()
    if request.method == 'POST':
        print('Printing POST', request.POST)
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    nombre = profe.Profesor.split(" ")[0] # Para mostrar solo el nombre del profesor
    context = {'profe' : profe,
                'form' : form,
                'nombreProfesor': nombre}
    
    return render(request, 'todoApp/anadir_menu.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'todoApp/delete.html', context)

def comandasGeneral(request):
    listaClases = Clase.objects.all()
    context = {'clases': listaClases}
    return render(request, 'todoApp/comandaGeneral.html', context)

def formularioComanda(request):
    listaMenus = Menu.objects.all()

    return render(request, "todoApp/{formularioMenusComedorAlberto}", {"lista" : listaMenus}) #AÑADIRLO CUANDO ALBERTO LO ESCOJA

def visualizarComanda(request):
    listaTotales = sumatorioMenus()
    return render(request, "todoApp/VisualizarComandaComedor.html", {"lista" : listaTotales}) #AÑADIRLO CUANDO SE SEPA