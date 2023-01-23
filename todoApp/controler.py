import pprint
from turtle import end_fill
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import *
from .funciones import *

fecha_visualizada = datetime.datetime.today().strftime("%Y-%m-%d")
dia_visualizado = datetime.datetime.today().strftime("%A")

def agenda(request,estudiante, fecha, dia):
    el = obtenerAlumno(estudiante)
    now = datetime.datetime.today().strftime("%Y-%m-%d")
    day = datetime.datetime.today().strftime("%A")
    
    fecha_formato =  datetime.datetime.strptime(fecha, "%Y-%m-%d")
    dia_formato = datetime.datetime.strptime(dia, "%A")

    tomorrow  = (fecha_formato + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    day_tomorrow = (fecha_formato + datetime.timedelta(days=1)).strftime("%A")

    yesterday = (fecha_formato - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    day_yesterday = (fecha_formato - datetime.timedelta(days=1)).strftime("%A")

    tareas = Pool.objects.filter(FechaIni__startswith=(fecha), Estudiante=el.id)
    context = {"tareas" : [], "dia_semana" : dia, "fecha" : fecha, "obj_estudiante" : el ,"estudiante" : estudiante, "prev": day_yesterday, "fecha_prev": yesterday, "pos":day_tomorrow, "fecha_pos":tomorrow}
    for tarea in tareas:
        tarea_real = Tarea.objects.get(Id = tarea.Tarea.Id)
        new_tarea = tarea.__dict__
        new_tarea["Descripcion"]=tarea_real.Descripcion
        new_tarea["Imagen"]=tarea_real.Imagen
        new_tarea["Tipo"] = tarea_real.Tipo
        context['tareas'].append(new_tarea)

    tasks = Tarea.objects.all()
    return render(request, 'todoApp/agenda.html', context)


def visualizar_tareas_txt(request, tarea, estudiante, fecha, dia):
    Tarea_seleccionada = Tarea.objects.get(Id = tarea)
    Pasos_de_la_tarea = Paso.objects.filter(Tarea_asociada=tarea)
    context = {'tarea' : Tarea_seleccionada, 'pasos' : Pasos_de_la_tarea, 'Estudiante' : estudiante , 'fecha' : fecha, 'dia' : dia}

    return render(request, 'todoApp/visualizar_tareas_txt.html', context)

def visualizar_tareas_img(request, tarea, estudiante, fecha, dia):
    Tarea_seleccionada = Tarea.objects.get(Id = tarea)
    Pasos_de_la_tarea = Paso.objects.filter(Tarea_asociada=tarea)
    context = {'tarea' : Tarea_seleccionada, 'pasos' : Pasos_de_la_tarea, 'Estudiante' : estudiante , 'fecha' : fecha, 'dia' : dia}

    return render(request, 'todoApp/visualizar_tareas_img.html', context)
    

def realizacion(request, estudiante, fecha, dia, resultado):
    context = {'Estudiante' : estudiante , 'fecha' : fecha, 'dia' : dia, 'resultado' : resultado}
    return render(request, 'todoApp/realizacion.html', context)

def index(request):
    lista_estudiantes = Estudiante.objects.all()
    context = {'estudiantes': lista_estudiantes}
    return render(request, 'todoApp/index.html', context)


def index_estudiante(request):
    return render(request, 'todoApp/index_estudiante.html')


def login_estudiante(request, estudiante):
    el = obtenerAlumno(estudiante)

    fecha = datetime.datetime.today().strftime("%Y-%m-%d")
    dia = datetime.datetime.today().strftime("%A")

    lista_passwords = ImagenPassword.objects.all()
    if request.method == 'POST':
        user = request.POST.get('nombre-estudiante')
        password = request.POST.get('password')
        isUser = obtenerAlumnoPassword(user, password)
        if isUser == "404":
            return render(request, 'todoApp/login_estudiante.html',
                          {'estudiante': el, 'imagenes': lista_passwords, 'error': True})
        else:
            return redirect('/alumno/agenda/' + el.Nombre + '/' + fecha + '/' + dia)
    return render(request, 'todoApp/login_estudiante.html',{'estudiante':el, 'imagenes': lista_passwords, 'error':False})


def index_profesor(request, profe):
    estudiantes = Estudiante.objects.all()
    tareas = Tarea.objects.all()
    profesor = Clase.objects.get(Profesor=profe)

    if request.method == 'POST':
        type = request.POST.get("oculta_number")
        if type == '2':
            cantidad = request.POST.get("cantidad_material")
            material = request.POST.get("nombre_material")
            imagen = request.POST.get("adjunto")
            print(cantidad,material,imagen)
        else:
            estus = request.POST.getlist('estudiante')
            task = request.POST.getlist('tarea')
            fecha_ini = request.POST.get('fecha_ini_id')
            fecha_fin = request.POST.get('fecha_ini_id_2')
            comanda_comedor = request.POST.get('checkbox_comedor')
            comanda_almacen = request.POST.get('checkbox_almacen')
            for est in estus:
                estud = obtenerAlumno(est)
                for tarea in task:
                    la_tarea =obtenerTarea(tarea)
                    Pool.objects.create(Estudiante=estud,Tarea=la_tarea,FechaFin=fecha_fin,FechaIni=fecha_ini)

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
