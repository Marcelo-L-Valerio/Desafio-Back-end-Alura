from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from releases.models.receitas import Receitas

class ReceitasTestCase(APITestCase):

    def setUp(self):

        self.list_url = reverse('Receitas-list')

        self.receita1= Receitas.objects.create(
            id=1, classificacao = "Venda", descricao='Televisao', valor=20000, dia= '2022-03-01'
        )

        self.receita2= Receitas.objects.create(
            id=2, classificacao = "Venda", descricao='Geladeira', valor=20000, dia= '2022-01-01'
        )

    def test_get_receita(self):
        """Teste para verificar requisisao GET para uma receita"""

        request = self.client.get(self.list_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(Receitas.objects.all().count(), 2)

        receita_usuario1 = request.data['results'][0]['classificacao']
        self.assertEqual(receita_usuario1, 'Venda')

    def test_get_receitas_de_um_mes(self):

        request = self.client.get(self.list_url + '2022/01/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        descricao = request.data['results'][0]['descricao']
        self.assertTrue(descricao == 'Geladeira')

    def test_get_receitas_por_descricao(self):

        request = self.client.get(self.list_url + '?search=Televisao')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        dia = request.data['results'][0]['dia']
        self.assertEqual(dia, '2022-03-01')

    def test_update_receita(self):

        request_antes = self.client.get(self.list_url + '1/')
        self.assertEqual(request_antes.data['valor'], 20000)

        data = {
            "classificacao": "Venda",
            "descricao":"Computador",
            "valor":10000,
            "dia":"2022-03-01"
        }

        request = self.client.put(self.list_url + '1/', data=data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        request_depois = self.client.get(self.list_url + '1/')
        self.assertEqual(request_depois.data['valor'], 10000)

    def test_delete_receita_por_id(self):

        request_antes = self.client.get(self.list_url + '1/')
        self.assertEqual(request_antes.status_code, status.HTTP_200_OK)

        request = self.client.delete(self.list_url + '1/')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

        request_depois = self.client.get(self.list_url + '1/')
        self.assertEqual(request_depois.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_receita(self):
        """Teste para verificar requisisao POST para criar uma receitas"""
        request_antes = self.client.get(self.list_url + '?search=Salario')
        self.assertEqual(request_antes.data['count'], 0)

        data = {
            "classificacao": "Salario",
            "descricao":"Salario",
            "valor":100000,
            "dia":"2022-01-01"
        }
        request = self.client.post(self.list_url, data=data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

        request_depois = self.client.get(self.list_url + '?search=Salario')
        self.assertEqual(request_depois.data['count'], 1)

    def test_post_receita_negado_dados_incompletos(self):

        data = {
            "classificacao": "Salario",
            "descricao":"Salario2",
            "valor":100000
        }
        request = self.client.post(self.list_url, data=data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_receita_negado_descricao_repetida_no_mes(self):

        data = {
            "classificacao": "Venda",
            "descricao":"Geladeira",
            "valor":10000,
            "dia":"2022-03-01"
        }

        request = self.client.post(self.list_url, data=data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)