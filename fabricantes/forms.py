from django import forms
from .models import Fabricantes


class FabricanteForm(forms.ModelForm):

    class Meta:
        model = Fabricantes
        fields = ['nome']

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control bg-light text-dark',
                'placeholder': 'Informe o nome do fabricante'
            })
        }