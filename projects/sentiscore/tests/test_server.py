import unittest
from unittest.mock import patch, Mock
from server import app, initialize_server

class TestServer(unittest.TestCase):

    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        app.debug = True
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        # Assertions to test the response of the index route

    def test_post_lookup_by_IDs_route(self):
        response = self.app.get('/2/tweets')
        # Assertions to test the response of the post_lookup_by_IDs route

    def test_post_lookup_by_ID_route(self):
        response = self.app.get('/2/tweets/123')
        # Assertions to test the response of the post_lookup_by_ID route

    def tearDown(self):
        if self.app_context:
            self.app_context.pop()

if __name__ == '__main__':
    unittest.main()

