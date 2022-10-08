
from rest_framework import generics
from releases.serializers.receitas_serializer import ReceitasSerializer
from releases.serializers.despesas_serializer import DespesasSerializer
from releases.models.receitas import Receitas
from releases.models.despesas import Despesas
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


class ReceitasMensaisViewSet(generics.ListAPIView):
    serializer_class = ReceitasSerializer
    
    def get_queryset(self):
        queryset = Receitas.objects.filter(dia__year=self.kwargs['ano'], dia__month=self.kwargs['mes'])
        return queryset
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]
    filterset_fields = ['classificacao']
    search_fields = ['descricao']

    authentication_classes = [BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    
class DespesasMensaisViewSet(generics.ListAPIView):
    serializer_class = DespesasSerializer
    
    def get_queryset(self):
        queryset = Despesas.objects.filter(dia__year=self.kwargs['ano'], dia__month=self.kwargs['mes'])
        return queryset
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter
    ]
    filterset_fields = ['classificacao']
    search_fields = ['descricao']

    authentication_classes = [BasicAuthentication]
    permission_classes = (IsAuthenticated,)