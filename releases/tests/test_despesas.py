from urllib import request
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from releases.models.despesas import Despesas

class DespesasTestCase(APITestCase):

    def setUp(self):

        self.list_url = reverse('Despesas-list')

        self.despesa1= Despesas.objects.create(
            id = 1, classificacao = "Alimentacao", descricao='Jantar', valor=20000, dia= '2022-03-01'
        )

        self.despesa2= Despesas.objects.create(
            id = 2, classificacao = "Alimentacao", descricao='Barraca de lanche', valor=20000, dia= '2022-01-01'
        )

    def test_get_despesa(self):
        """Teste para verificar requisisao GET para uma despesa"""

        request = self.client.get(self.list_url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(Despesas.objects.all().count(), 2)

        despesa_usuario1 = request.data['results'][0]['classificacao']
        self.assertEqual(despesa_usuario1, 'Alimentacao')

    def test_get_despesas_de_um_mes(self):

        request = self.client.get(self.list_url + '2022/01/')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        descricao = request.data['results'][0]['descricao']
        self.assertTrue(descricao == 'Barraca de lanche')

    def test_get_despesas_por_descricao(self):

        request = self.client.get(self.list_url + '?search=Jantar')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        dia = request.data['results'][0]['dia']
        self.assertEqual(dia, '2022-03-01')

    def test_update_despesa(self):

        request_antes = self.client.get(self.list_url + '1/')
        self.assertEqual(request_antes.data['valor'], 20000)

        data = {
            "classificacao": "Alimentacao",
            "descricao":"Fast Food",
            "valor":10000,
            "dia":"2022-03-01"
        }

        request = self.client.put(self.list_url + '1/', data=data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

        request_depois = self.client.get(self.list_url + '1/')
        self.assertEqual(request_depois.data['valor'], 10000)

    def test_delete_despesa_por_id(self):

        request_antes = self.client.get(self.list_url + '1/')
        self.assertEqual(request_antes.status_code, status.HTTP_200_OK)

        request = self.client.delete(self.list_url + '1/')
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)

        request_depois = self.client.get(self.list_url + '1/')
        self.assertEqual(request_depois.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_despesa(self):
        """Teste para verificar requisisao POST para criar uma despesa"""
        request_antes = self.client.get(self.list_url + '?search=Consulta')
        self.assertEqual(request_antes.data['count'], 0)

        data = {
            "classificacao": "Saude",
            "descricao":"Consulta",
            "valor":10000,
            "dia":"2022-01-01"
        }
        request = self.client.post(self.list_url, data=data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

        request_depois = self.client.get(self.list_url + '?search=Consulta')
        self.assertEqual(request_depois.data['count'], 1)

    def test_post_despesa_negado_dados_incompletos(self):

        data = {
            "classificacao": "Saude",
            "descricao":"Consulta",
            "valor":10000,
        }
        request = self.client.post(self.list_url, data=data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_despesa_negado_descricao_repetida_no_mes(self):

        data = {
            "tipo": "Despesas",
            "despesa": "Alimentacao",
            "descricao":"Jantar",
            "valor":10000,
            "dia":"2022-03-01",
            "usuario": 1
        }

        request = self.client.post(self.list_url, data=data)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)