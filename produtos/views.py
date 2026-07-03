from django.shortcuts import render, redirect
from .models import Produtos

# Create your views here.

def listar(request):
    produtos = Produtos.objects.all()

    return render(request, 'produtos/ListarProdutos.html', {
        'produtos': produtos
    })

def cadastro(request):
    return render(request, 'produtos/CadastroProdutos.html')

def excluir(request, codigo):
    try:
        produto = Produtos.objects.get(pk=codigo)
        produto.delete()
    except Produtos.DoesNotExist:
        pass

    return redirect('produtos:listar')