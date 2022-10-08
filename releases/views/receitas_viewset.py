
from rest_framework import viewsets
from releases.serializers.receitas_serializer import ReceitasSerializer
from releases.models.receitas import Receitas
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


class ReceitasViewSet(viewsets.ModelViewSet):
    queryset = Receitas.objects.all()
    serializer_class = ReceitasSerializer

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