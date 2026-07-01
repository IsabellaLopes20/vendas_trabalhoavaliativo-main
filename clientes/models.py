from django.db import models

# Create your models here.


class Clientes(models.Model):
    cpf = models.CharField(
        max_length=11,
        primary_key=True,
        help_text="Informe o CPF do cliente"
    )

    nome = models.CharField(
        max_length=70,
        null=False,
        blank=False,
        help_text="Informe o nome do cliente"
    )

    endereco = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text="Informe o endereço do cliente"
    )

    telefone = models.CharField(
        max_length=11,
        null=False,
        blank=False,
        help_text="Informe o telefone do cliente"
    )

    uf = models.CharField(
        max_length=2,
        null=False,
        blank=False,
        help_text="Informe a UF"
    )

    cidade = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        help_text="Informe a cidade"
    )

    genero = models.CharField(
        max_length=1,
        null=False,
        blank=False,
        help_text="Informe o gênero"
    )

    contato = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text="Informe o contato"
    )

    email = models.EmailField(
        max_length=100,
        unique=True,
        help_text="Informe o e-mail"
    )

    senha = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        help_text="Informe a senha"
    )

    class Meta:
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome