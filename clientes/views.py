from django.shortcuts import render, redirect, get_object_or_404
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
            dados = form.cleaned_data

            cliente = Clientes(
                cpf=dados['cpf'],
                nome=dados['nome'],
                endereco=dados['endereco'],
                telefone=dados['telefone'],
                uf=dados['uf'],
                cidade=dados['cidade'],
                genero=dados['genero'],
                contato=dados['contato'],
                email=dados['email'],
                senha=dados['senha']
            )

            cliente.save()

            return redirect('clientes:listar')

    else:
        form = ClienteForm()

    return render(request, 'clientes/CadastroClientes.html', {
        'form': form
    })


def excluir(request, cpf):
    try:
        cliente = Clientes.objects.get(pk=cpf)
        cliente.delete()
    except Clientes.DoesNotExist:
        pass

    return redirect('clientes:listar')


def editar(request, cpf):
    cliente = get_object_or_404(Clientes, cpf=cpf)

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            dados = form.cleaned_data

            cliente.cpf = dados['cpf']
            cliente.nome = dados['nome']
            cliente.endereco = dados['endereco']
            cliente.telefone = dados['telefone']
            cliente.uf = dados['uf']
            cliente.cidade = dados['cidade']
            cliente.genero = dados['genero']
            cliente.contato = dados['contato']
            cliente.email = dados['email']
            cliente.senha = dados['senha']

            cliente.save()

            return redirect('clientes:listar')

    else:
        form = ClienteForm(initial={
            'cpf': cliente.cpf,
            'nome': cliente.nome,
            'endereco': cliente.endereco,
            'telefone': cliente.telefone,
            'uf': cliente.uf,
            'cidade': cliente.cidade,
            'genero': cliente.genero,
            'contato': cliente.contato,
            'email': cliente.email,
            'senha': cliente.senha,
        })

    return render(request, 'clientes/CadastroClientes.html', {
        'form': form
    })


