from django.db import models
from fabricantes.models import Fabricantes


class Produtos(models.Model):
    codigo = models.AutoField(
        primary_key=True,
        help_text='Código do produto'
    )

    nome = models.CharField(
        max_length=70,
        null=False,
        blank=False,
        help_text='Informe o nome do produto'
    )


    preco_compra = models.FloatField(
        null=False,
        help_text='Informe o preço de compra'
    )

    preco_venda = models.FloatField(
        null=False,
        help_text='Informe o preço de venda'
    )

    cor = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        help_text='Informe a cor do produto'
    )

    imagem = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        help_text='Informe o nome da imagem'
    )

    fabricantes = models.ForeignKey(
        Fabricantes,
        on_delete=models.CASCADE,
        help_text='Informe o fabricante'
    )

    class Meta:
        db_table = 'produto'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome


