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

    def test_post_lookup_by_IDs_endpoint(self):
        ids = '1667982248614730000,1668031228811800000'
        response = self.app.get(f'/2/tweets?ids={ids}&tweet.fields=created_at,text&expansions=author_id&user.fields=username')
        self.assertEqual(response.status_code, 200)

        # If the endpoint returns JSON data, check the data:
        json_data = response.get_json()
        self.assertEqual(len(json_data), 2)

    def test_post_lookup_by_ID_endpoint(self):
        id = '1667982248614730000'
        response = self.app.get(f'/2/tweets/{id}?tweet.fields=created_at&expansions=author_id&user.fields=name')
        self.assertEqual(response.status_code, 200)

        # If the endpoint returns JSON data, check the data:
        json_data = response.get_json()
        self.assertEqual(len(json_data), 1)
        self.assertEqual(json_data['author']['name'], 'Elon Musk')
        self.assertEqual(json_data['author_id'], 44196397)

    def tearDown(self):
        if self.app_context:
            self.app_context.pop()

if __name__ == '__main__':
    unittest.main()

