from os import environ, path
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from .default_settings import *

sentry_sdk.init(
    dsn=environ.get('SENTRY_DSN', ''),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
)


DEBUG = False

ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS').split(',')

INSTALLED_APPS += [
    'api',
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

STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [path.join(BASE_DIR, 'static')]
