# encoding: utf-8

from django.test import TestCase


class BooksTest(TestCase):
    """
    Test the endpoints provided by the BooksViewSet.
    """
    def check_book_creation(self):
        response = self.client.post('/books', {
            'title': 'The Silmarillion',
            'author': 'J. R. R. Tolkien',
            'isbn': '9780061927645',
            'price': 10.40,
            'short_description': ("The Silmarillion is an account of the Elder Days, of the First Age of "
                                  "Tolkien's world.")
        })

        self.assertEquals(response.status_code, 201)
        # Check it has been assigned an ID
        self.assertIsInstance(response.data.get('id', None), int)

    def check_validations(self):
        # Try to insert the same ISBN again.
        response = self.client.post('/books', {
            'title': 'The Silmarillion',
            'author': 'J. R. R. Tolkien',
            'isbn': '9780061927645',
            'price': 11.00,
            'short_description': "Duplicated ISBN"
        })

        self.assertEquals(response.status_code, 400)
        self.assertIsInstance(response.data.get('isbn', None), list)

        # Try an isbn that is too long
        response = self.client.post('/books', {
            'title': 'The Silmarillion',
            'author': 'J. R. R. Tolkien',
            'isbn': '978006192764501',
            'price': 11.00,
            'short_description': "Long ISBN"
        })

        self.assertEquals(response.status_code, 400)
        self.assertIsInstance(response.data.get('isbn', None), list)

    def check_book_list_retrieval(self):
        response = self.client.get('/books')
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEquals(len(response.data), 1)

        book = response.data[0]
        self.assertIsInstance(book['id'], int)
        self.assertIsInstance(book.get('title', None), str)
        self.assertIsInstance(book.get('author', None), str)
        self.assertEquals('price' in book, True)
        self.assertIsInstance(book.get('short_description', None), str)

        # Save the ID of the retrieved book for subsequent tests.
        self.sample_book_id = book['id']

    def check_book_detail(self):
        # Return a single book information
        response = self.client.get('/books/{0}'.format(self.sample_book_id))
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.data, dict)
        self.assertEquals(response.data.get('id', None), self.sample_book_id)

    def check_filtering_title(self):
        response = self.client.get('/books', {'title': 'silmarill'})
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEquals(len(response.data) > 0, True)

        # Get the first item and check it has the searched item
        book = response.data[0]
        self.assertEquals('silmarill' in book['title'].lower(), True)

    def check_filtering_isbn(self):
        response = self.client.get('/books', {'isbn': '9780061927645'})
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        # ISBN is unique, one result should be found.
        self.assertEquals(len(response.data), 1)

        # Check it is indeed "The Silmarillion"
        book = response.data[0]
        self.assertEquals(book['isbn'], '9780061927645')

    def check_book_delete(self):
        response = self.client.delete('/books/{0}'.format(self.sample_book_id))
        self.assertEquals(response.status_code, 204)

        # Check the book with the sample ID has been deleted
        response = self.client.get('/books/{0}'.format(self.sample_book_id))
        self.assertEquals(response.status_code, 404)

    def test_book_endpoints(self):
        """
        This test method ensures tests are run in the proper order.
        """
        self.check_book_creation()
        self.check_validations()
        self.check_book_list_retrieval()
        self.check_book_detail()
        self.check_filtering_title()
        self.check_filtering_isbn()
        self.check_book_delete()

    def clear_throttling_rates(self):
        from django.core.cache import cache
        cache.clear()

    def test_throttling(self):
        self.clear_throttling_rates()
        # Assumes the default limit of 100 requests per day.
        for iteration in range(100):
            response = self.client.get('/books')
            self.assertEquals(response.status_code, 200)

        # The 101th request should be throttled.
        response = self.client.get('/books')
        self.assertEquals(response.status_code, 429)
