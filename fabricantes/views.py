from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def listar(request):
    return render(request, 'fabricantes/ListarFabricantes.html')

def cadastro(request):
    return render(request, 'fabricantes/CadastroFabricantes.html')