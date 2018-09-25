# encoding: utf-8

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from books import models, serializers


class BooksViewSet(ModelViewSet):
    """
    CRUD endpoints to manage books.
    """
    permission_classes = (AllowAny,)
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()
