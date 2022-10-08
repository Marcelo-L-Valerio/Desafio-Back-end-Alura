
from django.db import models

class Despesas(models.Model):

    DESPESAS = [
        ('Alimentacao', 'Alimentacao'),
        ('Saude', 'Saude'),
        ('Transporte', 'Transporte'),
        ('Roupas', 'Roupas'),
        ('Moradia', 'Moradia'),
        ('Lazer', 'Lazer'),
        ('Contas mensais', 'Contas mensais'),
        ('Eduacacao', 'Eduacacao'),
        ('Imprevistos', 'Imprevistos'),
        ('Outros', 'Outros')
    ]

    classificacao = models.CharField(max_length=14, choices=DESPESAS, null=True)
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