
from django.db import models

class Receitas(models.Model):

    RECEITAS = [
        ('Salario', 'Salario'),
        ('Venda', 'Venda'),
        ('Investimentos', 'Investimentos'),
        ('Outros', 'Outros')
    ]

    classificacao = models.CharField(max_length=13, choices=RECEITAS, null=True)
    descricao = models.CharField(max_length=100)
    valor = models.IntegerField()
    dia = models.DateField()

    @property
    def mes(self):
        return self.dia.strftime('%m')
    
    @property
    def ano(self):
        return self.dia.strftime('%Y')

    class Meta:
        ordering = ['id']