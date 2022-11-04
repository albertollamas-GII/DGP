from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Task)
admin.site.register(Menu)
admin.site.register(Clase)
admin.site.register(Solicita)