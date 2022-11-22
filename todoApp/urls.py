from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView

#from django.conf.urls import url

urlpatterns = [
    path('home/', views.index, name="index"),
    path('login/profesor/',views.login, name="login"),
    path('',views.login2,name="login2"),
    path('update_task/<str:pk>/', views.updateTask, name = "update_task"),
    path('delete/<str:pk>/', views.deleteTask, name = "delete"),
    path('comedor/anadir_menu/<str:clase>/', views.anadir_menu, name="anadir_menu"),
    path('comedor/anadir_menu/', views.anadir_menu, name="anadir_menu"),
    path('comedor/', views.comandasGeneral, name="comandaGeneral"),
    path('profesor/comanda/', views.visualizarComanda, name="menusTotalesProfesor"),

    #url(r'^favicon\.ico$',RedirectView.as_view(url='/static/favicon.ico'))

]