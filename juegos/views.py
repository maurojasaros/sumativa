from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegistroForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request,'juegos/index.html')

def formulario(request):
    return render(request,'juegos/formulario.html')

def aventuras(request):
    return render(request,'juegos/aventuras.html')

def deportes(request):
    return render(request,'juegos/deportes.html')

def rpg(request):
    return render(request,'juegos/rpg.html')

def shooter(request):
    return render(request,'juegos/shooter.html')

def terror(request):
    return render(request,'juegos/terror.html')

def inicio_sesion(request):
    return render(request, 'juegos/inicio_sesion.html')



def formulario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Procesar el formulario (igual que en registro_usuario)
            nombre_usuario = form.cleaned_data.get('nombre_usuario')
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            edad = form.cleaned_data.get('edad')
            direccion = form.cleaned_data.get('direccion')
            ciudad = form.cleaned_data.get('ciudad')

            # Crear el usuario en la base de datos
            user = User.objects.create_user(
                username=nombre_usuario,
                first_name=nombre,
                last_name=apellido,
                email=email,
                password=password
            )

            messages.success(request, 'Registro completado con éxito.')
            return redirect('login')  # Redirige a la página de inicio de sesión
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = RegistroForm()  # Si es una petición GET, crea un formulario vacío

    return render(request, 'juegos/formulario.html', {'form': form})

#@login_required
#def vista_protegida(request):
#    return render(request, 'juegos/rpg.html')