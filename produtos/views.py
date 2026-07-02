from django.shortcuts import render
from .models import Produtos

# Create your views here.

def listar(request):
    produtos = Produtos.objects.all()

    return render(request, 'produtos/ListarProdutos.html', {
        'produtos': produtos
    })

def cadastro(request):
    return render(request, 'produtos/CadastroProdutos.html')

