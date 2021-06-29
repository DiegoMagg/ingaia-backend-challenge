
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from empreendimento.models import Empreendimento
from api.serializers import (
    EmpreendimentoSerializer,
    ValorMetroQuadradoSerializer,
    ValorEmpreendimentoSerializer,
)


class ValorMetroQuadradoView(APIView):

    def get(self, request, nome):
        serializer = ValorMetroQuadradoSerializer(
            data=get_object_or_404(Empreendimento, nome=nome).__dict__,
        )
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class EmpreendimentoView(generics.ListAPIView):
    queryset = Empreendimento.objects.all()
    serializer_class = EmpreendimentoSerializer


class EmpreendimentoMetroQuadradoView(APIView):  # pragma: no cover

    def get(self, request, **kwargs):
        serializer = ValorEmpreendimentoSerializer(data=kwargs)
        serializer.is_valid(raise_exception=True)
        serializer.gera_valor_total_da_metragem_solicitada()
        return Response(serializer.validated_data)
