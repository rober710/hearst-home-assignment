# encoding: utf-8

from django_filters import rest_framework as drf_filters
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from books import filters, models, serializers


class BooksViewSet(ModelViewSet):
    """
    CRUD endpoints to manage books.
    """
    permission_classes = (AllowAny,)
    serializer_class = serializers.BookSerializer
    filter_backends = (drf_filters.DjangoFilterBackend, OrderingFilter)
    filter_class = filters.BooksViewSetFilter
    throttle_classes = (AnonRateThrottle,)
    queryset = models.Book.objects.all()
    ordering = ('title',)
