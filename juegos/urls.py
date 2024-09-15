from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView, agregar_al_carrito, ver_carrito, eliminar_del_carrito, realizar_pedido

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.formulario, name='formulario'),
    #path('aventuras/', views.aventuras, name='aventuras'),
    
    path('deportes/', views.deportes, name='deportes'),
    path('rpg/', views.rpg, name='rpg'),
    path('shooter/', views.shooter, name='shooter'),
    #path('terror/', views.terror, name='terror'),
    path('categoria/terror/', views.terror_view, name='categoria_terror'),
    path('categoria/aventuras/', views.aventuras_view, name='categoria_aventuras'),
    path('categoria/shooter/', views.shooter_view, name='categoria_shooter'),
    path('categoria/deportes/', views.deportes_view, name='categoria_deportes'),
    path('categoria/rpg/', views.rpg_view, name='categoria_rpg'),




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
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='juegos/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='juegos/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='juegos/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='juegos/password_reset_complete.html'), name='password_reset_complete'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('agregar_al_carrito/<int:juego_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', ver_carrito, name='ver_carrito'),
    path('eliminar_del_carrito/<int:item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('realizar_pedido/', realizar_pedido, name='realizar_pedido'),
    path('confirmacion_pedido/<int:pedido_id>/', views.confirmacion_pedido, name='confirmacion_pedido'),
   

]