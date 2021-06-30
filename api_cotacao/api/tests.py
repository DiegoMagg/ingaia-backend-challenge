from decimal import Decimal
from unittest.mock import patch
from rest_framework.test import APIClient
from django.test import TestCase
from api.serializers import CotacaoMetroQuadradoSerializer


class SerializersTestCase(TestCase):

    def test_serializer_deve_lancar_erro_caso_valor_informado_nao_permitido(self):
        serializer = CotacaoMetroQuadradoSerializer(
            data={'nome': 'teste', 'quantidade_metros_quadrados': 1},
        )
        self.assertFalse(serializer.is_valid())
        self.assertTrue('quantidade_metros_quadrados' in serializer.errors.keys())

    def test_serializer_deve_validar_valor_permitido(self):
        serializer = CotacaoMetroQuadradoSerializer(
            data={'nome': 'teste', 'quantidade_metros_quadrados': 100.00},
        )
        self.assertTrue(serializer.is_valid())


class IntegracaoTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    @patch('requests.get')
    def test_endpoint_cotacao_deve_retornar_valor_esperado(self, mock_get):
        mock_get.return_value.json.return_value = {
            'nome': 'empreendimento x',
            'valor_metro_quadrado': '1209.02'
        }
        serializer = CotacaoMetroQuadradoSerializer(
            data={'nome': 'teste', 'quantidade_metros_quadrados': 100.00},
        )
        serializer.is_valid()
        serializer.gera_valor_total_da_metragem_solicitada()
        self.assertEqual(
            dict(serializer.validated_data),
            {
                'nome': 'teste',
                'quantidade_metros_quadrados': Decimal('100.00'),
                'total': Decimal('120902.0000'),
            },
        )
