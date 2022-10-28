from .models import *

def obtenerListaClases(inicio,numero):

    start = chr(ord('@')+inicio)
    end = chr(ord('@')+inicio+numero)

    lista = Clase.objects.filter(letra__range=(start,end))

    return lista