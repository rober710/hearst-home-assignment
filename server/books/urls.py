# encoding: utf-8

"""
URLconfig for the books app.
"""

from rest_framework.routers import SimpleRouter

from books import views


books_router = SimpleRouter(trailing_slash=False)

books_router.register('books', views.BooksViewSet, base_name='books')

urlpatterns = books_router.urls
