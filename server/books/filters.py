# encoding: utf-8

"""
Filter classes for book app views.
"""

from django_filters import FilterSet, CharFilter

from books import models


class BooksViewSetFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')

    isbn = CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Book
        fields = ['title', 'isbn']
