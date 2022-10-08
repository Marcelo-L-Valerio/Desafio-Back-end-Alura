
from rest_framework import generics, serializers
from releases.models.receitas import Receitas
from releases.models.despesas import Despesas
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


class ResumoViewSet(generics.ListAPIView, serializers.ModelSerializer):
    '''Exibe o relatorio do mes'''
   
    def get(self, request, *args, **kwargs):
        
        receita_do_mes = Receitas.objects.filter(dia__year=self.kwargs['ano'], dia__month=self.kwargs['mes']).aggregate(
            Sum('valor'))['valor__sum'] or 0
        despesa_do_mes = Despesas.objects.filter(dia__year=self.kwargs['ano'], dia__month=self.kwargs['mes']).aggregate(
            Sum('valor'))['valor__sum'] or 0
        saldo = receita_do_mes - despesa_do_mes
        receita_por_categoria = Receitas.objects.filter(dia__year=self.kwargs['ano'], dia__month=self.kwargs['mes']).values('classificacao').annotate(Sum('valor'))
        despesa_por_categoria = Despesas.objects.filter(dia__year=self.kwargs['ano'], dia__month=self.kwargs['mes']).values('classificacao').annotate(Sum('valor'))

        for despesa in despesa_por_categoria:
            despesa['valor'] = despesa['valor__sum']
            del despesa['valor__sum']

        for receita in receita_por_categoria:
            receita['valor'] = receita['valor__sum']
            del receita['valor__sum']
        
        return Response({
            "Receita do Mês": f"R${receita_do_mes}",
            "Despesa do Mês": f"R${despesa_do_mes}",
            "Saldo Final do Mês": f"R${saldo}",
            "Gastos por Categoria": despesa_por_categoria,
            "Entradas por Categoria": receita_por_categoria
        })

    authentication_classes = [BasicAuthentication]
    permission_classes = (IsAuthenticated,)