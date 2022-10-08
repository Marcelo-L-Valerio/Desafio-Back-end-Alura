
from rest_framework import viewsets
from releases.serializers.despesas_serializer import DespesasSerializer
from releases.models.despesas import Despesas
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


class DespesasViewSet(viewsets.ModelViewSet):
    serializer_class = DespesasSerializer
    queryset = Despesas.objects.all()

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = ['descricao']
    filterset_fields = ['classificacao', 'dia']
    ordering_fields = ['dia']

    authentication_classes = [BasicAuthentication]
    permission_classes = (IsAuthenticated,)