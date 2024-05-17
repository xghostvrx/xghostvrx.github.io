import unittest
from unittest.mock import patch, Mock
import json

from server import app

class TestMockAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_posts_with_valid_arguments(self):
        response = self.app.get('/tweets?ids=1667982248614730000&tweet.fields=created_at,text&user.fields=username')
        self.assertEqual(response.status_code, 200)

        # If the endpoint returns JSON data, check the data:
        json_data = json.loads(response.data)
        self.assertIn('data', json_data)
        self.assertIn('meta', json_data)
        self.assertIn('newest_id', json_data['meta'])
        self.assertIn('oldest_id', json_data['meta'])
        self.assertIn('result_count', json_data['meta'])

    def test_get_posts_with_invalid_arguments(self):
        response = self.app.get('/tweets?ids=1,2,3&tweet.fields=created_at,text&user.fields=invalid_field')
        self.assertEqual(response.status_code, 400)

        # If the endpoint returns JSON data, check the error message:
        json_data = json.loads(response.data)
        self.assertIn('error', json_data)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
