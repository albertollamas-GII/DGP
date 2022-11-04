from .models import *


def sumatorioMenus():

    tipos_menu = Menu.objects.all()
    lista = []

    for menu in tipos_menu:
        solicitudes_por_menu = Solicita.objects.filter(TipoMenu = menu)
        total_por_menu = sum([solicita.Cantidad for solicita in solicitudes_por_menu])
        lista.append({"menu" : menu, "cantidad" :total_por_menu})

    #breakpoint()

    return lista