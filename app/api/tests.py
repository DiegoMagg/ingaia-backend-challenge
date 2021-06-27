from os import environ
from decimal import Decimal
from model_bakery import baker
from rest_framework.test import APIClient
from django.test import TestCase
from empreendimento.models import Empreendimento


class APITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        baker.make(
            Empreendimento,
            nome='empreendimento x',
            valor_metro_quadrado=Decimal(1000),
        )

    def test_empreendimento_deve_ser_criado_no_endpoint(self):
        data = {'nome': 'Empreendimento Teste', 'valor_metro_quadrado': Decimal(1000)}
        self.client.post('/empreendimento', data)
        self.assertTrue(Empreendimento.objects.filter(**data).exists())

    def test_endpoint_valor_metro_quadrado_deve_retornar_status_200(self):
        response = self.client.get('/valor-metro-quadrado/empreendimento x')
        self.assertEqual(response.status_code, 200)

    def test_endpoint_valor_metro_quadrado_deve_retornar_json_esperado(self):
        saida_esperada = {'nome': 'empreendimento x', 'valor_metro_quadrado': 'R$1.000,00'}
        response = self.client.get('/valor-metro-quadrado/empreendimento x')
        self.assertEqual(response.json(), saida_esperada)
