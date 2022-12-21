from sys import maxsize
from django.db import models
import datetime

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
    FotoProfesor = models.ImageField(upload_to="static/imagenes/profesores/")
    Password = models.CharField(max_length=100)
    FotoClase = models.ImageField(upload_to="static/imagenes/clases/", null = True)
    Check = models.BooleanField( default = False)

    def __str__(self):
        return self.Letra + "-" +  self.Profesor 

class Menu(models.Model):
    Tipo = models.CharField(
        max_length = 100,
        help_text = "Introducir el tipo de menu",
        primary_key = True
    )

    Imagen = models.ImageField(upload_to="static/imagenes/menus/")

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
    
    Imagen = models.ImageField(upload_to="static/imagenes/numeros/")

class Estudiante(models.Model):
    Nombre = models.CharField(max_length = 100)
    Imagen = models.ImageField(upload_to="static/imagenes/estudiantes/")
    Password = models.CharField(max_length=1000)
    ModoImagen = models.BooleanField( default = False)
    def __str__(self):
        return self.Nombre

class Historico(models.Model):

    Fecha_ini = models.DateField()

    Fecha_fin = models.DateField()

    Documento = models.FileField(upload_to="static/imagenes/menusAnteriores/")

class ImagenPassword(models.Model):
    Imagen = models.ImageField(upload_to="static/imagenes/imagen_password")
    Nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.Nombre

class Tarea(models.Model):
    Id = models.AutoField(
        auto_created=True,
        primary_key=True
    )
    Descripcion = models.CharField(max_length=50)
    Imagen = models.ImageField(upload_to="static/imagenes/tareas", null=True)

    def __str__(self):
        return f'{self.Id} - {self.Descripcion}'
    

class Paso(models.Model):
    Descripcion = models.CharField(max_length=250)
    Imagen = models.ImageField(upload_to="static/imagenes/pasos")
    Tarea_asociada = models.ForeignKey(
        "Tarea",
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f'Paso:{self.Descripcion} - Tarea:{self.Tarea_asociada}'

class Pool(models.Model):
    Estudiante = models.ForeignKey(
        "Estudiante",
        on_delete=models.CASCADE
    )
    Tarea = models.ForeignKey(
        "Tarea",
        on_delete=models.CASCADE
    )
    Check = models.BooleanField( default = False)

    FechaIni = models.DateField(default = datetime.date.today())
    FechaFin = models.DateField(default = datetime.date.today() + datetime.timedelta(days=2))
    
    def __str__(self):
        return f'Tarea:{self.Tarea} - Estudiante:{self.Estudiante} - {self.Check}'