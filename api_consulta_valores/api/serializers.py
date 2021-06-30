from rest_framework import serializers
from empreendimento.models import Empreendimento
from django.utils.formats import localize



class ValorMetroQuadradoSerializer(serializers.Serializer):
    nome = serializers.CharField(min_length=4, max_length=60)
    valor_metro_quadrado = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_valor_metro_quadrado(self, valor):
        return self.trata_valores_monetarios(valor)

    @staticmethod
    def trata_valores_monetarios(valor, casas_decimais=2):
        return f'R${localize(round(valor, casas_decimais))}'
