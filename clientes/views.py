from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from .models import Clientes
from .forms import ClienteForm


def listar(request):
    clientes = Clientes.objects.all()

    return render(request, 'clientes/ListarClientes.html', {
        'clientes': clientes
    })


def cadastro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            cliente = form.save(commit=False)

            # Gera o hash da senha
            cliente.senha = make_password(form.cleaned_data['senha'])

            cliente.save()

            return redirect('clientes:listar')

    else:
        form = ClienteForm()

    return render(request, 'clientes/CadastroClientes.html', {
        'form': form
    })


def excluir(request, cpf):
    cliente = get_object_or_404(Clientes, pk=cpf)
    cliente.delete()

    return redirect('clientes:listar')


def editar(request, cpf):
    cliente = get_object_or_404(Clientes, cpf=cpf)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            cliente = form.save(commit=False)

            # Gera o hash da senha novamente
            cliente.senha = make_password(form.cleaned_data['senha'])

            cliente.save()

            return redirect('clientes:listar')

    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/CadastroClientes.html', {
        'form': form
    })