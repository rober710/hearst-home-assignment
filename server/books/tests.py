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

    def check_book_detail(self):
        # Return a single book information
        book_id = 1
        response = self.client.get('/books/{0}'.format(book_id))
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.data, dict)
        self.assertEquals(response.data.get('id', None), book_id)

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
