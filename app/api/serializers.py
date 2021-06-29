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

    def validate_quantidade_metros_quadrados(self, quantidade):
        if quantidade not in range(10, 10001):
            raise serializers.ValidationError(
                'A quantidade de metros quadrados deve estar entre 10 e 10000.',
            )
        return quantidade

    def gera_valor_total_da_metragem_solicitada(self):  # pragma: no cover
        queryset = get_object_or_404(Empreendimento, nome=self.data['nome'])
        json = requests.get(
            f'https://{environ["API_URL"]}/{environ["API_VERSION"]}/'
            f'valor-metro-quadrado/{queryset.nome}',
        ).json()
        valor_metro_quadrado = Decimal(
            json['valor_metro_quadrado'].replace('.', '').replace(',', '.')[2:],
        )
        total = self.validated_data['quantidade_metros_quadrados'] * valor_metro_quadrado
        self.validated_data['total'] = self.trata_valores_monetarios(total)
