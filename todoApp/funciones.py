from .models import *


def sumatorioMenus():

    tipos_menu = Menu.objects.all()
    lista = []

    for menu in tipos_menu:
        solicitudes_por_menu = Solicita.objects.filter(TipoMenu = menu)
        total_por_menu = sum([solicita.Cantidad for solicita in solicitudes_por_menu])
        if total_por_menu > 0:
            lista.append({"menu": menu, "cantidad": total_por_menu})
    return lista

def obtenerProfesor(nombre,password):
    clases = Clase.objects.all()

    for profesor in clases:
        if profesor.Profesor == nombre and profesor.Password == password:
            return profesor
    return "404"

def obtenerAlumno(nombre):
    alumnos_totales = Estudiante.objects.all()

    for estudiante in alumnos_totales:
        if estudiante.Nombre == nombre:
            return estudiante
    return "not found"

def obtenerAlumnoPassword(nombre, password):
    alumnos_totales = Estudiante.objects.all()

    for estudiante in alumnos_totales:
        if estudiante.Nombre == nombre and estudiante.Password == password:
            return estudiante
    return "404"





