
from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from loteamento.models import Loteamento
from django.shortcuts import get_object_or_404
from api.serializers import ValorLoteamentoSerializer


class LoteamentoMetroQuadradoView(APIView):

    def get(self, request, **kwargs):
        serializer = ValorLoteamentoSerializer(data=kwargs)
        serializer.is_valid(raise_exception=True)
        serializer.gera_valor_total_da_metragem_solicitada()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
