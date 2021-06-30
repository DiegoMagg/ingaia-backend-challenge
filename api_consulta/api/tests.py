from decimal import Decimal
from model_bakery import baker
from rest_framework.test import APIClient
from django.test import TestCase
from empreendimento.models import Empreendimento


class APITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.empreendimento = baker.make(
            Empreendimento,
            nome='teste',
            valor_metro_quadrado=Decimal(1000),
        )

    def test_endpoint_valor_metro_quadrado_deve_retornar_json_esperado(self):
        saida_esperada = {'nome': 'teste', 'valor_metro_quadrado': '1000.00'}
        response = self.client.get('/v1/valor-metro-quadrado/teste')
        self.assertEqual(response.json(), saida_esperada)
