
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import CotacaoMetroQuadradoSerializer


class EmpreendimentoMetroQuadradoView(APIView):  # pragma: no cover

    def get(self, request, **kwargs):
        serializer = CotacaoMetroQuadradoSerializer(data=kwargs)
        serializer.is_valid(raise_exception=True)
        serializer.gera_valor_total_da_metragem_solicitada()
        return Response(serializer.validated_data)
