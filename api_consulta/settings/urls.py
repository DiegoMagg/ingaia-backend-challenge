from os import environ
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

API_VERSION = environ.get('API_VERSION')

DESCRIPTION = '''
    Esta api é uma demonstração do desafio backend proposto pela inGaia e
    estará disponível para avaliação até 09/07/2021.
'''

api_version_one = get_schema_view(
    openapi.Info(
        title='API de consulta de preço por metro quadrado',
        description=DESCRIPTION,
        default_version=API_VERSION,
    ),
    url=environ.get('API_URL'),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(f'{API_VERSION}/', api_version_one.with_ui('swagger', cache_timeout=0)),
    path(f'{API_VERSION}/', include('api.urls')),
]
