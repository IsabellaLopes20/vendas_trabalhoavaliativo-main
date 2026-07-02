from django import forms

class ClienteForm(forms.Form):
    cpf = forms.CharField(
        max_length=11,
        required=True,
        help_text='Informe o CPF do cliente'
    )

    nome = forms.CharField(
        max_length=70,
        required=True,
        help_text='Informe o nome do cliente'
    )

    endereco = forms.CharField(
        max_length=100,
        required=True,
        help_text='Informe o endereço do cliente'
    )

    telefone = forms.CharField(
        max_length=11,
        required=True,
        help_text='Informe o telefone do cliente'
    )

    uf = forms.CharField(
        max_length=2,
        required=True,
        help_text='Informe a UF do cliente'
    )

    cidade = forms.CharField(
        max_length=50,
        required=True,
        help_text='Informe a cidade do cliente'
    )

    genero = forms.CharField(
        max_length=1,
        required=True,
        help_text='Informe o gênero do cliente'
    )

    contato = forms.CharField(
        max_length=100,
        required=True,
        help_text='Informe o contato do cliente'
    )

    email = forms.EmailField(
        required=True,
        help_text='Informe o e-mail do cliente'
    )

    senha = forms.CharField(
        max_length=256,
        required=True,
        help_text='Informe a senha do cliente'
    )