from django.shortcuts import render, redirect, get_object_or_404
from .models import Produtos
from .forms import ProdutoForm
from fabricantes.models import Fabricantes


def listar(request):
    produtos = Produtos.objects.all()

    return render(request, 'produtos/ListarProdutos.html', {
        'produtos': produtos
    })


def cadastro(request):

    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            dados = form.cleaned_data

            produto = Produtos(
                nome=dados['nome'],
                preco_compra=dados['preco_compra'],
                preco_venda=dados['preco_venda'],
                cor=dados['cor'],
                fabricantes=dados['fabricantes']
            )

            produto.save()

            return redirect('produtos:listar')

    else:
        form = ProdutoForm()

    fabricantes = Fabricantes.objects.all()

    return render(request, 'produtos/CadastroProdutos.html', {
        'form': form,
        'fabricantes': fabricantes
    })


def excluir(request, codigo):
    try:
        produto = Produtos.objects.get(pk=codigo)
        produto.delete()
    except Produtos.DoesNotExist:
        pass

    return redirect('produtos:listar')


def editar(request, codigo):
    produto = get_object_or_404(Produtos, codigo=codigo)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)

        if form.is_valid():
            form.save()
            return redirect('produtos:listar')

    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'produtos/CadastroProdutos.html', {
        'form': form
    })