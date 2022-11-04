from turtle import end_fill
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import *
from .funciones import *

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todoApp/index.html', context)

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

def anadir_menu(request):
    return render(request, 'todoApp/anadir_menu.html')

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'todoApp/delete.html', context)

def comandasGeneral(request):
    listaClases = Clase.objects.all()

    return render(request, 'todoApp/comandaGeneral.html', {"lista" : listaClases})

def formularioComanda(request):
    listaMenus = Menu.objects.all()

    return render(request, "todoApp/{formularioMenusComedorAlberto}", {"lista" : listaMenus}) #AÑADIRLO CUANDO ALBERTO LO ESCOJA

def visualizarComanda(request):
    listaTotales = sumatorioMenus()
    return render(request, "todoApp/VisualizarComandaComedor.html", {"lista" : listaTotales}) #AÑADIRLO CUANDO SE SEPA