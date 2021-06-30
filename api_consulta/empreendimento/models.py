from django.db import models


DB_TABLE = 'empreendimento'


class Empreendimento(models.Model):
    nome = models.CharField(max_length=60, unique=True)
    valor_metro_quadrado = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = DB_TABLE
        verbose_name = DB_TABLE
        verbose_name_plural = f'{DB_TABLE}s'
