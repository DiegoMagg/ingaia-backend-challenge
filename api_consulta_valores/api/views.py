
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404
from empreendimento.models import Empreendimento
from api.serializers import ValorMetroQuadradoSerializer


class ValorMetroQuadradoView(APIView):

    def get(self, request, nome):
        serializer = ValorMetroQuadradoSerializer(
            data=get_object_or_404(Empreendimento, nome=nome).__dict__,
        )
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
