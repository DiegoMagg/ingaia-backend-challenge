from os import environ
from decimal import Decimal
from copy import deepcopy
from model_bakery import baker
from rest_framework.test import APIClient
from django.test import TestCase
from empreendimento.models import Empreendimento
from api.serializers import ValorEmpreendimentoSerializer


class SerializersTestCase(TestCase):

    def test_serializer_deve_lancar_erro_caso_valor_informado_nao_permitido(self):
        serializer = ValorEmpreendimentoSerializer(
            data={'nome': 'teste', 'quantidade_metros_quadrados': 1},
        )
        self.assertFalse(serializer.is_valid())
        self.assertTrue('quantidade_metros_quadrados' in serializer.errors.keys())

    def test_serializer_deve_validar_valor_permitido(self):
        serializer = ValorEmpreendimentoSerializer(
            data={'nome': 'teste', 'quantidade_metros_quadrados': 100.00},
        )
        self.assertTrue(serializer.is_valid())


class APITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.empreendimento = baker.make(
            Empreendimento,
            nome='empreendimento x',
            valor_metro_quadrado=Decimal(1000),
        )

    def test_empreendimento_deve_ser_criado_no_endpoint(self):
        data = {'nome': 'Empreendimento Teste', 'valor_metro_quadrado': Decimal(1000)}
        self.client.post('/v1/empreendimento', data)
        self.assertTrue(Empreendimento.objects.filter(**data).exists())

    def test_endpoint_valor_metro_quadrado_deve_retornar_json_esperado(self):
        saida_esperada = {'nome': 'empreendimento x', 'valor_metro_quadrado': 'R$1.000,00'}
        response = self.client.get('/v1/valor-metro-quadrado/empreendimento x')
        self.assertEqual(response.json(), saida_esperada)
