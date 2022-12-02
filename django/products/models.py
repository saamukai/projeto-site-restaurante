from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    disponivel = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.nome)

class Produto (models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150, verbose_name="Descrição")
    preco = models.DecimalField(decimal_places=2, max_digits=6)
    disponivel = models.BooleanField()

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return "{} {} ({})".format(self.nome, self.preco, self.descricao)
