from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientes
from .forms import ClienteForm

def listar(request):
    clientes = Clientes.objects.all()

    return render(request, 'clientes/ListarClientes.html', {
        'clientes': clientes
    })

def cadastro(request):
    return render(request, 'clientes/CadastroClientes.html')

def excluir(request, cpf):
    try:
        cliente = Clientes.objects.get(pk=cpf)
        cliente.delete()
    except Clientes.DoesNotExist:
        pass

    return redirect('clientes:listar')


