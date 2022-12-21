import pprint
from turtle import end_fill
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import *
from .funciones import *

def agenda(request,estudiante):
    el = obtenerAlumno(estudiante)
    tareas = Pool.objects.filter(Estudiante=el.id)
    context = {"tareas" : []}
    for tarea in tareas:
        tarea_real = Tarea.objects.get(Id = tarea.Tarea.Id)
        new_tarea = tarea.__dict__
        new_tarea["Descripcion"]=tarea_real.Descripcion
        new_tarea["Imagen"]=tarea_real.Imagen
        context['tareas'].append(new_tarea) 
    return render(request, 'todoApp/agenda.html', context)

def visualizar_tareas_txt(request):
    return render(request, 'todoApp/visualizar_tareas_txt.html')

def visualizar_tareas_img(request, tarea):
    Estu = Pool.objects.get(Tarea = tarea).Estudiante
    Tarea_seleccionada = Tarea.objects.get(Id = tarea)
    Pasos_de_la_tarea = Paso.objects.filter(Tarea_asociada=tarea)
    context = {'tarea' : Tarea_seleccionada, 'pasos' : Pasos_de_la_tarea, 'Estudiante' : Estu }
    return render(request, 'todoApp/visualizar_tareas_img.html', context)

def index(request):
    lista_estudiantes = Estudiante.objects.all()
    context = {'estudiantes': lista_estudiantes}
    return render(request, 'todoApp/index.html', context)


def index_estudiante(request):
    return render(request, 'todoApp/index_estudiante.html')



def login_estudiante(request, estudiante):
    el = obtenerAlumno(estudiante)
    lista_passwords = ImagenPassword.objects.all()
    if request.method == 'POST':
        user = request.POST.get('nombre-estudiante')
        password = request.POST.get('password')
        isUser = obtenerAlumnoPassword(user,password)
        if isUser == "404":
            return render(request, 'todoApp/login_estudiante.html',{'estudiante':el, 'imagenes': lista_passwords, 'error': True})
        else:
            return redirect('/alumno/agenda/' + el.Nombre)
    return render(request, 'todoApp/login_estudiante.html',{'estudiante':el, 'imagenes': lista_passwords, 'error':False})

def index_profesor(request,profe):
    estudiantes = Estudiante.objects.all()
    tareas = Tarea.objects.all()  

    if request.method == 'POST':
        estus = request.POST.getlist('estudiante')
        task = request.POST.get('tarea')
        fecha_ini = request.POST.get('fecha_ini')
        fecha_fin = request.POST.get('fecha_fin')
        print(estus, task,fecha_fin,fecha_ini)
        

    if request.method == 'POST':
        return render(request,'todoApp/index_profesor.html',{'profesor':profe,'estudiantes':estudiantes,'tareas':tareas})
    else:
        return render(request,'todoApp/index_profesor.html',{'profesor':profe,'estudiantes':estudiantes,'tareas':tareas})    
    
    


def login_profesor(request):
    
    if request.method == 'POST':
        user = request.POST.get('text')
        password = request.POST.get('pwd')
        profe = obtenerProfesor(user, password)
        if profe == '404':
            return render(request, 'todoApp/login_profesor.html', {'isUser': False})
        else:
            return index_profesor(request,profe)

    return render(request, 'todoApp/login_profesor.html', {'isUser': True})


def anadir_menu(request, clase='Clase de Ejemplo'):
    profe = Clase.objects.get(Letra=clase)
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
        return comanda_general(request)
    else:
        return render(request, 'todoApp/anadir_menu.html', context)


def comanda_general(request):
    listaClases = Clase.objects.all()
    context = {'clases': listaClases}
    return render(request, "todoApp/comanda_general.html", context)


def visualizar_comanda(request):
    listaTotales = sumatorioMenus()
    return render(request, "todoApp/visualizar_comanda_comedor.html", {"lista": listaTotales})  # AÑADIRLO CUANDO SE SEPA
