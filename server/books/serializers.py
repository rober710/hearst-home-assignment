# encoding: utf-8

"""
Serializers used in the books app.
"""

from rest_framework import serializers

from books import models


class BookSerializer(serializers.ModelSerializer):
    """
    Serializers and deserializes book instances.
    """
    class Meta:
        model = models.Book
        fields = '__all__'
