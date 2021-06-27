from os import environ
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

API_VERSION = environ.get('API_VERSION')

DESCRIPTION = '''
    Esta api é uma demonstração do desafio backend proposto pela inGaia e
    estará disponível para avaliação até 02/07/2021.
'''

schema_view = get_schema_view(
    openapi.Info(
        title='API Imobiliária',
        description=DESCRIPTION,
        default_version=API_VERSION,
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0)),
    path('', include('api.urls')),
]
