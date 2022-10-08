# from http.client import ResponseNotReady
# from rest_framework.test import APITestCase, APIClient
# from rest_framework import status
# from django.urls import reverse
# from releases.models.lancamentos import Lancamentos
# from releases.models.usuario import Usuario

# class LancamentosTestCase(APITestCase):

#     def setUp(self):

#         self.list_url = reverse('Lancamentos-list')

#         self.usuario1 = Usuario.objects.create(nome='Marcelo', cpf='99336641077', saldo=10000)
#         self.usuario2 = Usuario.objects.create(nome='Jonas', cpf='37207023081', saldo=10000)

#         self.receita1= Lancamentos.objects.create(
#             tipo = "Receitas", receita = "Investimentos", descricao='Investimentos bolsa', valor=30000, dia= '2022-01-01', usuario= self.usuario1
#         )
#         self.despesa1= Lancamentos.objects.create(
#             tipo = "Despesas", despesa = "Alimentacao", descricao='Jantar 01/01', valor=20000, dia= '2022-01-01', usuario= self.usuario1
#         )

#         self.receita2= Lancamentos.objects.create(
#             tipo = "Receitas", receita = "Venda", descricao='Geladeira', valor=30000, dia= '2022-01-01', usuario= self.usuario2
#         )
#         self.despesa2= Lancamentos.objects.create(
#             tipo = "Despesas", despesa = "Alimentacao", descricao='Barraca de lanche', valor=20000, dia= '2022-01-01', usuario= self.usuario2
#         )
    
#     def test_post_usuario(self):
#         print(self.list_url)
#         request = self.client.post(self.list_url, data= {
#             "tipo": "Receitas",
#             "despesa": "",
#             "receita": "Salario",
#             "descricao": "Salario9",
#             "valor": 15002,
#             "dia": "2022-09-30",
#             "usuario":1
#         })
#         print(Lancamentos.objects.all())
#         self.assertEqual(request.status_code, status.HTTP_201_CREATED)

#         # descricao = 

#     def test_get_despesa(self):
#         """Teste para verificar requisisao GET para uma despesa"""

#         request = self.client.get('/despesas/')
#         self.assertEqual(request.status_code, status.HTTP_200_OK)
#         self.assertEqual(Lancamentos.objects.filter(tipo="Despesas").count(), 2)

#         despesa_usuario1 = request.data['results'][0]['despesa']
#         self.assertEqual(despesa_usuario1, 'Alimentacao')