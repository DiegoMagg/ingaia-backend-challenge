from rest_framework import serializers
from django.utils.formats import localize
from django.shortcuts import get_object_or_404
from loteamento.models import Loteamento


class ValorLoteamentoSerializer(serializers.Serializer):
    nome = serializers.CharField()
    quantidade_metros_quadrados = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
    )

    def validate_nome(self, nome):
        self.queryset = get_object_or_404(Loteamento, nome__icontains=nome)
        return nome

    def validate_quantidade_metros_quadrados(self, quantidade):
        if quantidade not in range(10, 10001):
            raise serializers.ValidationError(
                'A quantidade de metros quadrados deve estar entre 10 e 10000.',
            )
        return quantidade

    def gera_valor_total_da_metragem_solicitada(self):
        valor_metro_quadrado = self.queryset.valor_metro_quadrado
        total = (
            self.validated_data["quantidade_metros_quadrados"] *
            valor_metro_quadrado
        )
        self.validated_data['valor_do_metro_quadrado'] = f'R${localize(round(valor_metro_quadrado, 2))}'
        self.validated_data['total'] = f'R${localize(round(total, 2))}'
