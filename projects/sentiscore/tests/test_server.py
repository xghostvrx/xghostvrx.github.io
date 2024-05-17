import unittest
from unittest.mock import patch, Mock

import flask
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
        self.assertEqual(response.status_code, 200)

    def test_index_route_template(self):
        with self.app as c:
            c.get('/')
            self.assertEqual(flask.request.endpoint, 'index')

    def tearDown(self):
        if self.app_context:
            self.app_context.pop()

if __name__ == '__main__':
    unittest.main()

