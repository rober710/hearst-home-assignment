# encoding: utf-8

from django.conf.urls import url

from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from books.urls import urlpatterns as book_urls

schema_view = get_schema_view(
    openapi.Info(
        title='Books API',
        default_version='v1',
        description='Home assignment API',
        contact=openapi.Contact(name='Roberto Balarezo', email='roberto.balarezo@jobsity.com'),
        license=openapi.License(name='BSD License')
    ),
    public=True,
    permission_classes=(AllowAny,)
)

api_urls = [
    url(r'^$', schema_view.without_ui(cache_timeout=0), name='index'),
    url(r'^docs$', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    url(r'^redoc$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

urlpatterns = api_urls + book_urls
