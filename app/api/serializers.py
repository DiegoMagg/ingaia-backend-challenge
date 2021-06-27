import requests
from os import environ, stat
from decimal import Decimal
from rest_framework import serializers
from django.utils.formats import localize
from django.shortcuts import get_object_or_404
from empreendimento.models import Empreendimento


class EmpreendimentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empreendimento
        fields = ['nome', 'valor_metro_quadrado']


class BaseValorMetroSerializer(serializers.Serializer):
    nome = serializers.CharField(min_length=4, max_length=60)

    @staticmethod
    def trata_valores_monetarios(valor, casas_decimais=2):
        return f'R${localize(round(valor, casas_decimais))}'


class ValorMetroQuadradoSerializer(BaseValorMetroSerializer):
    valor_metro_quadrado = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_valor_metro_quadrado(self, valor):
        return self.trata_valores_monetarios(valor)


class ValorEmpreendimentoSerializer(BaseValorMetroSerializer):
    quantidade_metros_quadrados = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    def validate_nome(self, nome):
        self.queryset = get_object_or_404(Empreendimento, nome__icontains=nome)
        return nome

    def validate_quantidade_metros_quadrados(self, quantidade):
        if quantidade not in range(10, 10001):
            raise serializers.ValidationError(
                'A quantidade de metros quadrados deve estar entre 10 e 10000.',
            )
        return quantidade

    def gera_valor_total_da_metragem_solicitada(self):
        response = requests.get(
            f'{environ["API_BASE_URL"]}/valor-metro-quadrado/{self.queryset.nome}',
        )
        valor_metro_quadrado = Decimal(response.json()['valor_metro_quadrado'])
        total = self.validated_data['quantidade_metros_quadrados'] * valor_metro_quadrado
        self.validated_data['total'] = self.trata_valores_monetarios(total)
