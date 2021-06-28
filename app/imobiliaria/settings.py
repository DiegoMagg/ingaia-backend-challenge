from os import environ
from .default_settings import *

DEBUG = False

ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS', 'localhost').split(',')

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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
