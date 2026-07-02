from django.shortcuts import render
from .models import Clientes

def listar(request):
    clientes = Clientes.objects.all()

    return render(request, 'clientes/ListarClientes.html', {
        'clientes': clientes
    })

def cadastro(request):
    return render(request, 'clientes/CadastroClientes.html')