from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=username)
        if user is not None:
            # El usuario ha sido autenticado, así que lo redirigimos a la página de inicio.
            return redirect('inicio')
        else:
            error_message = 'Nombre de usuario y contraseña Correctos.'
    else:
        error_message = ''
    return render(request, 'core/index.html', {'error_message': error_message})

def inicio(request):
    return render(request, 'core/inicio.html', {})

def acercade(request):
    return render(request, 'core/acercade.html', {})

def miproyecto(request):
    return render(request, 'core/miproyecto.html', {})

def contacto(request):
    return render(request, 'core/contacto.html', {})


# Create your views here.
