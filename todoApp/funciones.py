from .models import *


def sumatorioMenus():

    tipos_menu = Menu.objects.all()
    lista = []

    for menu in tipos_menu:
        solicitudes_por_menu = Solicita.objects.filter(TipoMenu = menu)
        total_por_menu = sum([solicita.Cantidad for solicita in solicitudes_por_menu])
        if total_por_menu > 0:
            lista.append({"menu": menu, "cantidad": total_por_menu})

    #breakpoint()

    return lista

def obtenerAlumno(nombre):
    alumnos_totales = Estudiante.objects.all()

    for estudiante in alumnos_totales:
        if estudiante.Nombre.__contains__(nombre):
            return estudiante
        else:
            return "not found"
