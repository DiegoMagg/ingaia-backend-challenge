from .default_settings import *


ALLOWED_HOSTS = ['localhost']

INSTALLED_APPS += [
    'api',
    'loteamento',
    'drf_yasg',
]

USE_I18N = True

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_TZ = True

USE_L10N = True

USE_THOUSAND_SEPARATOR = True
