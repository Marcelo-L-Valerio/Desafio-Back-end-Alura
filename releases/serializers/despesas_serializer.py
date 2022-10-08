from rest_framework import serializers
from releases.models.despesas import Despesas
from releases.validators.lancamentos_validators import *


class DespesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesas
        fields = '__all__'

    def validate(self, data):

        if not descricao_valida(data['descricao']):
            raise serializers.ValidationError({'descricao':'Descricao nao deve ser vazio'})
        
        if not valor_valido(data['valor']):
            raise serializers.ValidationError({'valor':'O valor deve ser maior que 0 (mesmo para despesas)'})

        if not valor_numerico(data['valor']):
            raise serializers.ValidationError({'valor':'O valor deve ser um inteiro (R$ 10.00 = 1000)'})

        if not descricao_unica_valida(data, Despesas):
            raise serializers.ValidationError({'descricao':'Descricao deve ser unica no mes'})

        if not dia_valido(data['dia']):
            raise serializers.ValidationError({'dia':'O dia deve ser um date field'})

        return data
