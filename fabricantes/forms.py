from django import forms

class FabricanteForm(forms.Form):
    nome = forms.CharField(
        max_length=70,
        required=True,
        help_text='Informe o nome do fabricante'
    )