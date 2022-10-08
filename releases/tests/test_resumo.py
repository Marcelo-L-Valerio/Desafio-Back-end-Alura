from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from releases.models.receitas import Receitas
from releases.models.despesas import Despesas

class LancamentosTestCase(APITestCase):

    def setUp(self):

        self.list_url = reverse('Resumo', kwargs={'ano': '2022', 'mes': '01'})

        self.receita1= Receitas.objects.create(
            id=1, classificacao = "Venda", descricao='Televisao', valor=20000, dia= '2022-03-01'
        )

        self.receita2= Receitas.objects.create(
            id=2, classificacao = "Salario", descricao='Geladeira', valor=20000, dia= '2022-01-01'
        )

        self.despesa1= Despesas.objects.create(
            id = 1, classificacao = "Alimentacao", descricao='Jantar', valor=20000, dia= '2022-03-01'
        )

        self.despesa2= Despesas.objects.create(
            id = 2, classificacao = "Educacao", descricao='Barraca de lanche', valor=10000, dia= '2022-01-01'
        )

    def test_gerar_resumo_de_um_mes(self):

        request = self.client.get(self.list_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        self.assertEqual(request.data['Saldo Final do Mês'], 'R$10000')

    def test_get_detalhamento_receitas(self):

        request = self.client.get(self.list_url)

        self.assertEqual(request.data['Entradas por Categoria'][0]['classificacao'], 'Salario')
        self.assertEqual(request.data['Entradas por Categoria'][0]['valor'], 20000)

    def test_get_detalhamento_despesas(self):

        request = self.client.get(self.list_url)

        self.assertEqual(request.data['Gastos por Categoria'][0]['classificacao'], 'Educacao')
        self.assertEqual(request.data['Gastos por Categoria'][0]['valor'], 10000)