from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegistroForm
from .forms import JuegoForm #Tengo que hacer un formulario para cada juego

# Create your views here.
def index(request):
    return render(request, 'juegos/index.html')

def formulario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('nombre_usuario')
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            # Crear el usuario en la base de datos
            user = User.objects.create_user(
                username=nombre_usuario,
                first_name=nombre,
                last_name=apellido,
                email=email,
                password=password
            )
            
            # Iniciar sesión automáticamente después del registro
            login(request, user)
            
            messages.success(request, 'Registro completado con éxito. Has iniciado sesión automáticamente.')
            return redirect('index')  # Redirige a la página principal o a donde desees
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = RegistroForm()  # Si es una petición GET, crea un formulario vacío

    return render(request, 'juegos/formulario.html', {'form': form})

def aventuras(request):
    return render(request, 'juegos/aventuras.html')

def deportes(request):
    return render(request, 'juegos/deportes.html')

def rpg(request):
    return render(request, 'juegos/rpg.html')

def shooter(request):
    return render(request, 'juegos/shooter.html')

def terror(request):
    return render(request, 'juegos/terror.html')

def inicio_sesion(request):
    return render(request, 'juegos/inicio_sesion.html')

# Listar juegos
def listar_juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'juegos/listar_juegos.html', {'juegos': juegos})

# Ver detalles de un juego
def ver_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    return render(request, 'juegos/ver_juego.html', {'juego': juego})

# Crear un nuevo juego
def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_juegos')
    else:
        form = JuegoForm()
    return render(request, 'juegos/crear_juego.html', {'form': form})

# Editar un juego existente
def editar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'POST':
        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('ver_juego', pk=juego.pk)
    else:
        form = JuegoForm(instance=juego)
    return render(request, 'juegos/editar_juego.html', {'form': form})

# Eliminar un juego
def eliminar_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    if request.method == 'POST':
        juego.delete()
        return redirect('listar_juegos')
    return render(request, 'juegos/eliminar_juego.html', {'juego': juego})