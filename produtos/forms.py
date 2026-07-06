from django import forms
from .models import Produtos
from fabricantes.models import Fabricantes


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produtos
        fields = [
            'nome',
            'preco_compra',
            'preco_venda',
            'cor',
            'fabricantes'
        ]

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control bg-light text-dark',
                'placeholder': 'Informe o nome do produto'
            }),

            'preco_compra': forms.NumberInput(attrs={
                'class': 'form-control bg-light text-dark',
                'placeholder': 'Informe o preço de compra'
            }),

            'preco_venda': forms.NumberInput(attrs={
                'class': 'form-control bg-light text-dark',
                'placeholder': 'Informe o preço de venda'
            }),

            'cor': forms.TextInput(attrs={
                'class': 'form-control bg-light text-dark',
                'placeholder': 'Informe a cor'
            }),

            'fabricantes': forms.Select(attrs={
                'class': 'form-control'
            }),
        }