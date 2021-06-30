from django.urls import path
from api.views import ValorMetroQuadradoView

app_name = 'api'

urlpatterns = [
    path(
        'valor-metro-quadrado/<str:nome>',
        ValorMetroQuadradoView.as_view(),
        name='valor-metro-quadrado',
    ),
]
