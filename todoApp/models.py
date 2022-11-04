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
    FotoProfesor = models.ImageField(upload_to="imagenes/clases")

    def __str__(self):
        return self.Letra + "-" +  self.Profesor

class Menu(models.Model):
    Tipo = models.CharField(
        max_length = 100,
        help_text = "Introducir el tipo de menu",
        primary_key = True
    )

    Imagen = models.ImageField(upload_to="iamgenes/menus")

    def __str__(self):
        return self.Tipo


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

    def __str__(self):
        clase = self.Clase_asociada
        menu = self.TipoMenu
        canti = self.Cantidad

        return str(self.Clase_asociada) + " solicita " + str(self.Cantidad) + " de " + str(self.TipoMenu)

class Numero(models.Model):
    Numero = models.IntegerField(primary_key=True)
    
    Imagen = models.ImageField(upload_to="imagenes/manos")

    def __str__(self):
        return self.Imagen

class Estudiante(models.Model):
    Nombre = models.CharField(max_length = 100)

    Imagen = models.ImageField(upload_to="imagenes/estudiantes")

    def __str__(self):
        return self.Nombre

class Historico(models.Model):

    Fecha_ini = models.DateField()

    Fecha_fin = models.DateField()

    Documento = models.FileField(upload_to="docs/historico")