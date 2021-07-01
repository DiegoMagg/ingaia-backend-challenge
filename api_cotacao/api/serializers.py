import requests
from os import environ
from decimal import Decimal
from rest_framework import serializers
from django.http import Http404


class CotacaoMetroQuadradoSerializer(serializers.Serializer):
    nome = serializers.CharField(min_length=4, max_length=60)
    quantidade_metros_quadrados = serializers.IntegerField(min_value=10, max_value=10000)

    def gera_valor_total_da_metragem_solicitada(self):  # pragma: no cover
        url = (
            f'{environ["API_CONSULTA_URL"]}/'
            f'valor-metro-quadrado/{self.validated_data.get("nome")}'
        )
        response = requests.get(url)
        if not response.ok:
            raise Http404(response.json()['detail'])
        valor_metro_quadrado = Decimal(response.json()['valor_metro_quadrado'])
        self.validated_data['total'] = (
            self.validated_data['quantidade_metros_quadrados'] * valor_metro_quadrado
        )
