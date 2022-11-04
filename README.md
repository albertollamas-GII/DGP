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

5. Para ejecutar el proyecto
   > python manage.py runserver y entrar a: http://127.0.0.1:8000/

6. Para añadir nuevas tablas
   > python manage.py migrate --fake todoApp zero
   > eliminar todos los todoApp/migrations/000x_loquesea.py MENOS __init__py
   > python manage.py makemigrations
   > python manage.py migrate

**YA ESTÁ DJANGO CONFIGURADO**

## ¿Cómo programamos en Django?

