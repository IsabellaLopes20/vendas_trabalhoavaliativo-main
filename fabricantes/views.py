from django.shortcuts import render, redirect
from .models import Fabricantes

# Create your views here.

def listar(request):
    fabricantes = Fabricantes.objects.all()

    return render(request, 'fabricantes/ListarFabricantes.html', {
        'fabricantes': fabricantes
    })

def cadastro(request):
    return render(request, 'fabricantes/CadastroFabricantes.html')

def excluir(request, codigo):
    try:
        fabricante = Fabricantes.objects.get(pk=codigo)
        fabricante.delete()
    except Fabricantes.DoesNotExist:
        pass

    return redirect('fabricantes:listar')