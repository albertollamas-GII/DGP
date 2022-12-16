# APNE (Aplicación Para Personas con Necesidades Especiales)

## ¿Cómo instalar Django?

1. Asegurarnos de que tenemos Python instalado
   > py --version <br>

Si no está instalado -> [pulsa aquí](https://docs.python.org/3/using/windows.html)

2. Instalar Django
   > pip install django==3.2 (u otra versión posterior)

3. Hacer un *git clone* del (repositorio)[https://github.com/albertollamass/GII-DGP]
   > git clone (dependiendo de si teneis ssh configurado o no coger un link u otro)

4. Entrar en el repositorio clonado y ejecutar lo siguiente:
   > pip install whitenoise
   > pip install django-extensions
   > pip install pygraphviz (si estais en ubuntu hay que hacer sudo apt-get install algo, buscad en internet: "instalar pygraphviz ubuntu")
   > pip install Pillow
   > Si os da problema con tkinter o algo asi, buscad instalación en Google.

5. Para ejecutar el proyecto
   > python manage.py runserver y entrar a: http://127.0.0.1:8000/

6. Para añadir nuevas tablas
   > python manage.py makemigrations
   > python manage.py migrate

**YA ESTÁ DJANGO CONFIGURADO**

## ¿Cómo programamos en Django?
**Cosas importantes**
* Para crear usuario administrador:
  > python manage.py createsuperuser
* Para entrar a la página de administrador entrar a http://127.0.0.1:8000/admin con el superusuario creado anteriormente.
* Si no sale el CSS de la página de administrador:
  * Entramos en learnDjango/settings.py y modificamos DEBUG = True.
  * Puede que con esto no aparezcan las imágenes, para ello lo ponemos a False.

Lo siguiente ya es pelearse con Python.

Models.py -> modelo
Views.py -> controlador
En templates/ hacer los htmls

