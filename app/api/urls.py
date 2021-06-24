from django.urls import path
from api.views import LoteamentoMetroQuadradoView

app_name = 'api'

urlpatterns = [
    path(
        'cotacao/<str:nome>/<int:quantidade_metros_quadrados>',
        LoteamentoMetroQuadradoView.as_view(),
        name='cotacao-loteamento',
    ),
]
