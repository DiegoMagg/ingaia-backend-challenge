
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from empreendimento.models import Empreendimento
from api.serializers import ValorMetroQuadradoSerializer


class ValorMetroQuadradoView(APIView):

    def get(self, request, nome):
        serializer = ValorMetroQuadradoSerializer(
            instance=get_object_or_404(Empreendimento, nome=nome),
        )
        return Response(serializer.data)
