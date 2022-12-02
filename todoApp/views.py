import pprint
from turtle import end_fill
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import *
from .funciones import *


def index(request):
    return render(request, 'todoApp/index.html')



def password_estudiante(request, estudiante):
    el = obtenerAlumno(estudiante)
    lista_passwords = ImagenPassword.objects.all()
    if request.method == 'POST':
        user = request.POST.get('nombre-estudiante')
        password = request.POST.get('password')
        isUser = obtenerAlumnoPassword(user,password)
        if isUser == "404":
            return render(request, 'todoApp/password_estudiante.html',{'estudiante':el, 'imagenes': lista_passwords, 'error': True})
        else:
            return index(request)
    return render(request, 'todoApp/password_estudiante.html',{'estudiante':el, 'imagenes': lista_passwords, 'error':False})

def asignar_tareas(request,profe):

    estudiantes = Estudiante.objects.all()
    tareas = Task.objects.all()  # TODO ASIGNAR EL POOL DE TAREAS (NO SE SI ES Task)
    return render(request,'todoApp/asignar_tareas.html',{'profesor':profe,'estudiantes':estudiantes,'tareas':tareas})

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
    if request.method == 'POST':
        user = request.POST.get('text')
        password = request.POST.get('pwd')
        profe = obtenerProfesor(user, password)
        if profe == '404':
            return render(request, 'todoApp/login.html', {'isUser': False})
        else:
            return asignar_tareas(request,profe)

    return render(request, 'todoApp/login.html', {'isUser': True})


def login2(request):
    lista_estudiantes = Estudiante.objects.all()
    context = {'estudiantes': lista_estudiantes}
    return render(request, 'todoApp/login2.html', context)


def anadir_menu(request, clase='Clase de Ejemplo'):
    profe = obtenerClase(clase)
    numeros = Numero.objects.all()
    solicitudes = Solicita.objects.filter(Clase_asociada=profe.Letra)
    menus = Menu.objects.all()
    for menu in menus:
        menu.Tipo = menu.Tipo.upper
    form = MenuForm()

    if request.method == 'POST':
        Cantidades = request.POST.getlist('Cantidad')
        profe.Check = True
        profe.save()
        for sol, cantidad in zip(solicitudes, Cantidades):
            sol.Cantidad = cantidad
            sol.save()

    nombre = profe.Profesor.split(" ")[0]  # Para mostrar solo el nombre del profesor
    context = {'profe': profe,
               'form': form,
               'nombreProfesor': nombre.upper,
               'menus': menus,
               'numeros': numeros,
               'solicitudes': solicitudes}

    if request.method == 'POST':
        return comandasGeneral(request)
    else:
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

    return render(request, "todoApp/{formularioMenusComedorAlberto}",
                  {"lista": listaMenus})  # AÑADIRLO CUANDO ALBERTO LO ESCOJA


def visualizarComanda(request):
    listaTotales = sumatorioMenus()
    return render(request, "todoApp/VisualizarComandaComedor.html", {"lista": listaTotales})  # AÑADIRLO CUANDO SE SEPA
