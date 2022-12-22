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
    now = datetime.datetime.today().strftime("%Y-%m-%d")
    day = datetime.datetime.today().strftime("%A")

    tareas = Pool.objects.filter(FechaIni__startswith=(now), Estudiante=el.id)
    context = {"tareas" : [], "dia_semana" : day, "estudiante" : estudiante}
    for tarea in tareas:
        tarea_real = Tarea.objects.get(Id = tarea.Tarea.Id)
        new_tarea = tarea.__dict__
        new_tarea["Descripcion"]=tarea_real.Descripcion
        new_tarea["Imagen"]=tarea_real.Imagen
        context['tareas'].append(new_tarea) 
    return render(request, 'todoApp/agenda.html', context)

def agendamas(request,estudiante):
    el = obtenerAlumno(estudiante)
    day = datetime.datetime.today().strftime("%A")

    if ( day != "Friday"):
        tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        day_after = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%A")
    else:
        tomorrow = (datetime.date.today() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")
        day_after = (datetime.date.today() + datetime.timedelta(days=3)).strftime("%A")


    tareas = Pool.objects.filter(FechaIni__startswith=(tomorrow), Estudiante=el.id)
    context = {"tareas" : [], "dia_semana" : day_after, "estudiante" : estudiante}
    for tarea in tareas:
        tarea_real = Tarea.objects.get(Id = tarea.Tarea.Id)
        new_tarea = tarea.__dict__
        new_tarea["Descripcion"]=tarea_real.Descripcion
        new_tarea["Imagen"]=tarea_real.Imagen
        context['tareas'].append(new_tarea) 
    return render(request, 'todoApp/agenda.html', context)

def agendamenos(request,estudiante):
    el = obtenerAlumno(estudiante)
    day = datetime.datetime.today().strftime("%A")

    if ( day != "Monday"):
        yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        day_yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%A")
    else:
        yesterday = (datetime.date.today() - datetime.timedelta(days=3)).strftime("%Y-%m-%d")
        day_yesterday = (datetime.date.today() - datetime.timedelta(days=3)).strftime("%A")


    tareas = Pool.objects.filter(FechaIni__startswith=(yesterday), Estudiante=el.id)
    context = {"tareas" : [], "dia_semana" : day_yesterday, "estudiante" : estudiante}
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
        isUser = obtenerAlumnoPassword(user, password)
        if isUser == "404":
            return render(request, 'todoApp/login_estudiante.html',
                          {'estudiante': el, 'imagenes': lista_passwords, 'error': True})
        else:
            return redirect('/alumno/agenda/' + el.Nombre)
    return render(request, 'todoApp/login_estudiante.html',{'estudiante':el, 'imagenes': lista_passwords, 'error':False})


def index_profesor(request, profe):
    estudiantes = Estudiante.objects.all()
    tareas = Tarea.objects.all()
    profesor = Clase.objects.get(Profesor=profe)

    if request.method == 'POST':
        estus = request.POST.getlist('estudiante')
        task = request.POST.getlist('tarea')
        fecha_ini = request.POST.get('fecha_ini_id')
        fecha_fin = request.POST.get('fecha_fin_id')

        print(estus, task, fecha_fin, fecha_ini)

    return render(request, 'todoApp/index_profesor.html',
                  {'profesor': profe, 'estudiantes': estudiantes, 'tareas': tareas})


def login_profesor(request):
    if request.method == 'POST':
        user = request.POST.get('text')
        password = request.POST.get('pwd')
        profe = obtenerProfesor(user, password)
        if profe == '404':
            return render(request, 'todoApp/login_profesor.html', {'isUser': False})
        else:
            return redirect('/profesor/'+profe.Profesor)

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
    return render(request, "todoApp/visualizar_comanda_comedor.html",
                  {"lista": listaTotales})  # AÑADIRLO CUANDO SE SEPA
