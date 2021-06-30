from rest_framework import serializers
from empreendimento.models import Empreendimento


class ValorMetroQuadradoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empreendimento
        fields = ['nome', 'valor_metro_quadrado']
