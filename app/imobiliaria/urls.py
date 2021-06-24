from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(title='Real State API', default_version='v1'),
)

urlpatterns = [
    path(r'', schema_view.with_ui('swagger', cache_timeout=0)),
    path(r'', include('api.urls')),
]
