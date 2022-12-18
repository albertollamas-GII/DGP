from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Menu)
admin.site.register(Clase)
admin.site.register(Solicita)
admin.site.register(Numero)
admin.site.register(Estudiante)
admin.site.register(Historico)
admin.site.register(ImagenPassword)
admin.site.register(Tarea)
admin.site.register(Paso)
admin.site.register(Pool)