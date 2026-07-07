from django import forms
from .models import Clientes


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = [
            'cpf',
            'nome',
            'endereco',
            'telefone',
            'uf',
            'cidade',
            'genero',
            'contato',
            'email',
            'senha'
        ]

        widgets = {
            'cpf': forms.TextInput(attrs={
                'class': 'form-control bg-light text-dark',
                'placeholder': 'Informe o CPF do cliente'
            }),

            'nome': forms.TextInput(attrs={
                'class': 'form-control bg-light text-dark',
                'placeholder': 'Informe o nome do cliente'
            }),

            'endereco': forms.TextInput(attrs={
                'class': 'form-control bg-light text-dark',
                'placeholder': 'Informe o endereço do cliente'
            }),

            'telefone': forms.TextInput(attrs={
                'class': 'form-control bg-light text-dark',
                'placeholder': 'Informe o telefone do cliente'
            }),

           'uf': forms.Select(attrs={
               'class': 'form-control bg-light text-dark'
            }),

           'cidade': forms.Select(attrs={
               'class': 'form-control bg-light text-dark'
            }),

           'genero': forms.Select(attrs={
               'class': 'form-control bg-light text-dark'
            }),

            'contato': forms.TextInput(attrs={
                'class': 'form-control bg-light text-dark',
                'placeholder': 'Informe o contato'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-light text-dark',
                'placeholder': 'Informe o e-mail'
            }),

            'senha': forms.PasswordInput(attrs={
                'class': 'form-control bg-light text-dark',
                'placeholder': 'Informe a senha'
            }),
        }