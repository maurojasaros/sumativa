from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.formulario, name='formulario'),
    path('aventuras/', views.aventuras, name='aventuras'),
    path('deportes/', views.deportes, name='deportes'),
    path('rpg/', views.rpg, name='rpg'),
    path('shooter/', views.shooter, name='shooter'),
    path('terror/', views.terror, name='terror'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('lista_juegos/', views.listar_juegos, name='listar_juegos'),
    path('juegos/crear', views.crear_juego, name='crear_juego'),
    path('juegos/ver/<int:pk>/',views.ver_juego, name='ver_juego'),
    path('juegos/editar/<int:pk>/', views.editar_juego, name='editar_juego'), #se especifica la primary key pk el id
    path('juegos/eliminar/<int:pk>/', views.eliminar_juego, name='eliminar_juego'), #se especifica la primary key pk el id
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('lista_categorias/', views.listar_categorias, name='listar_categorias'),
    path('categorias/editar/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
   

]