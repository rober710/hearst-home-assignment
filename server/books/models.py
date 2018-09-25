# encoding: utf-8

from django.db import models


class Book(models.Model):
    """
    Stores book information.
    """
    title = models.CharField(max_length=200)

    author = models.CharField(max_length=250)

    isbn = models.CharField(max_length=13, unique=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    short_description = models.TextField(blank=True)

    def __str__(self):
        return '({0}) {1}'.format(self.isbn, self.title)

    class Meta:
        ordering = ['title']
