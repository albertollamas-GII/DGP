from sys import maxsize
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

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
        max_length = 2, 
        help_text = "Introducir la Letra de la Clase", 
        primary_key = True,
        unique = True
    )
    Profesor = models.CharField(
        max_length = 100,
        help_text = "Introduce el nombre del profesor asignado"
    )

class Menu(models.Model):
    Tipo = models.CharField(
        max_length = 100,
        help_text = "Introducir el tipo de menu",
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

    Cantidad = models.IntegerField()

