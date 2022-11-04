from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('update_task/<str:pk>/', views.updateTask, name = "update_task"),
    path('delete/<str:pk>/', views.deleteTask, name = "delete"),
    path('comedor/anadir_menu/<str:pk>/', views.formularioComanda, name="anadir_menu"),
    path('comedor/', views.comandasGeneral, name="comandaGeneral"),
    path('profesor/comanda/', views.visualizarComanda, name="menusTotalesProfesor")
]