# Generated by Django 4.1.3 on 2022-11-24 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0004_alter_clase_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imagen', models.ImageField(upload_to='static/imagen_password')),
                ('Nombre', models.CharField(max_length=100)),
            ],
        ),
    ]