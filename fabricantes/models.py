from django.db import models

# Create your models here.
class Fabricantes(models.Model):
    codigo = models.AutoField(
        primary_key=True,
        help_text="Código do fabricante"
    )

    nome = models.CharField(
        max_length=70,
        null=False,
        blank=False,
        help_text="Nome do fabricante"
    )

    class Meta:
        verbose_name = "Fabricantes"
        verbose_name_plural = "Fabricantes"

    def __str__(self):
        return self.nome