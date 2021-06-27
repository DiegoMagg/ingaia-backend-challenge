from django.urls import path
from api.views import (
    EmpreendimentoView,
    ValorMetroQuadradoView,
    EmpreendimentoMetroQuadradoView,
)

app_name = 'api'

urlpatterns = [
    path(
        'valor-metro-quadrado/<str:nome>',
        ValorMetroQuadradoView.as_view(),
        name='valor-metro-quadrado',
    ),
    path(
        'cotacao/<str:nome>/<int:quantidade_metros_quadrados>',
        EmpreendimentoMetroQuadradoView.as_view(),
        name='cotacao',
    ),
    path(
        'empreendimento',
        EmpreendimentoView.as_view(),
        name='cotacao',
    ),
]
