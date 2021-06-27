from .default_settings import *


ALLOWED_HOSTS = ['localhost']

INSTALLED_APPS += [
    'api',
    'empreendimento',
    'drf_yasg',
    'rest_framework',
]

USE_I18N = True

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_TZ = True

USE_L10N = True

USE_THOUSAND_SEPARATOR = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
