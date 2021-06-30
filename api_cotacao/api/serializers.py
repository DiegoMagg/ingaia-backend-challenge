import requests
from os import environ
from decimal import Decimal
from rest_framework import serializers


class CotacaoMetroQuadradoSerializer(serializers.Serializer):
    nome = serializers.CharField(min_length=4, max_length=60)
    quantidade_metros_quadrados = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    def validate_quantidade_metros_quadrados(self, quantidade):
        if quantidade not in range(10, 10001):
            raise serializers.ValidationError(
                'A quantidade de metros quadrados deve ser entre 10 e 10000.',
            )
        return quantidade

    def gera_valor_total_da_metragem_solicitada(self):  # pragma: no cover
        url = (
            f'{environ["API_CONSULTA_URL"]}/'
            f'valor-metro-quadrado/{self.validated_data.get("nome")}'
        )
        response = requests.get(url)
        valor_metro_quadrado = Decimal(response.json()['valor_metro_quadrado'])
        self.validated_data['total'] = (
            self.validated_data['quantidade_metros_quadrados'] * valor_metro_quadrado
        )
