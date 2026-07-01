from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def listar(request):
    return render(request, 'produtos/ListarProdutos.html')

def cadastro(request):
    return render(request, 'produtos/CadastroProdutos.html')

