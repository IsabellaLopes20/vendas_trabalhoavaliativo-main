from django import forms
from fabricantes.models import Fabricantes

class ProdutoForm(forms.Form):

    nome = forms.CharField(
        max_length=70,
        required=True,
        help_text='Informe o nome do produto'
    )

    preco_compra = forms.FloatField(
        required=True,
        help_text='Informe o preço de compra'
    )

    preco_venda = forms.FloatField(
        required=True,
        help_text='Informe o preço de venda'
    )

    cor = forms.CharField(
        max_length=20,
        required=True,
        help_text='Informe a cor do produto'
    )

    fabricantes = forms.ModelChoiceField(
        queryset=Fabricantes.objects.all(),
        required=True,
        empty_label='Selecione um fabricante'
    )