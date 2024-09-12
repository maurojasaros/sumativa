from django.shortcuts import render

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
