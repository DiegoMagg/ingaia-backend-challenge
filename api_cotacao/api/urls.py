from django.urls import path
from api.views import EmpreendimentoMetroQuadradoView

app_name = 'api'

urlpatterns = [
    path(
        'cotacao/<str:nome>/<int:quantidade_metros_quadrados>',
        EmpreendimentoMetroQuadradoView.as_view(),
        name='cotacao',
    ),

]
