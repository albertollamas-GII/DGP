from sys import maxsize
from django.db import models

# Create your models here.
class OpcionesVisualizacion:
    Opciones = (
        (0,"Ninguna"),
        (1,"Lectura"),
        (2,"Vision"),
        (3,"Motora")
    )

    Tipo = models.IntegerField(
        choices = Opciones,
        default=0
    )
   
class Clase(models.Model):
    Letra = models.CharField(   
        maxsize = "2", 
        helptext = "Introducir la Letra de la Clase", 
        primary_key = True,
        unique = True
    )
    Profesor = models.CharField(
        maxsize = "100",
        helptext = "Introduce el nombre del profesor asignado"
    )

class Menu(models.Model):
    Tipo = models.CharField(
        maxsize = "100",
        helptext = "Introducir el tipo de menu",
        primary_key = True
    )

    Imagen = models.ImageField()


class Solicita(models.Model):    
    Clase_asociada = models.ForeignKey(
        "Clase",
        on_delete = models.CASCADE
    )

    TipoMenu = models.ForeignKey(
        "Menu",
        on_delete = models.CASCADE
    )

    Cantidad = models.IntegerField(
        empty_strings_allowed = False
    )

