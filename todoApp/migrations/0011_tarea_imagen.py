# Generated by Django 3.2 on 2022-12-21 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0010_auto_20221221_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='Imagen',
            field=models.ImageField(null=True, upload_to='static/imagenes/tareas'),
        ),
    ]
