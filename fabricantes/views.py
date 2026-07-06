from django.shortcuts import render, redirect, get_object_or_404
from .models import Fabricantes
from .forms import FabricanteForm


def listar(request):
    fabricantes = Fabricantes.objects.all()

    return render(request, 'fabricantes/ListarFabricantes.html', {
        'fabricantes': fabricantes
    })


def cadastro(request):
    if request.method == 'POST':
        form = FabricanteForm(request.POST)

        if form.is_valid():
            dados = form.cleaned_data

            fabricante = Fabricantes(
                nome=dados['nome']
            )

            fabricante.save()

            return redirect('fabricantes:listar')

    else:
        form = FabricanteForm()

    return render(request, 'fabricantes/CadastroFabricantes.html', {
        'form': form
    })


def excluir(request, codigo):
    try:
        fabricante = Fabricantes.objects.get(pk=codigo)
        fabricante.delete()
    except Fabricantes.DoesNotExist:
        pass

    return redirect('fabricantes:listar')

def editar(request, codigo):
    fabricante = get_object_or_404(Fabricantes, codigo=codigo)

    if request.method == 'POST':
        form = FabricanteForm(request.POST)

        if form.is_valid():
            dados = form.cleaned_data

            fabricante.nome = dados['nome']
            fabricante.save()

            return redirect('fabricantes:listar')

    else:
        form = FabricanteForm(initial={
            'nome': fabricante.nome
        })

    return render(request, 'fabricantes/CadastroFabricantes.html', {
        'form': form
    })