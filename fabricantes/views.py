from django.shortcuts import render
from .models import Fabricantes

# Create your views here.

def listar(request):
    fabricantes = Fabricantes.objects.all()

    return render(request, 'fabricantes/ListarFabricantes.html', {
        'fabricantes': fabricantes
    })

def cadastro(request):
    return render(request, 'fabricantes/CadastroFabricantes.html')