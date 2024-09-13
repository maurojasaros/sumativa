from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.formulario, name='formulario'),
    path('aventuras/', views.aventuras, name='aventuras'),
    path('deportes/', views.deportes, name='deportes'),
    path('rpg/', views.rpg, name='rpg'),
    path('shooter/', views.shooter, name='shooter'),
    path('terror/', views.terror, name='terror'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
   

]