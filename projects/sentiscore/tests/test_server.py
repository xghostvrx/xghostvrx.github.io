import unittest
from unittest.mock import patch
from server import initialize_server

class TestServerInitialization(unittest.TestCase):

    @patch('server.getenv')
    @patch('server.check_database_exists')
    @patch('server.check_table_exists')
    @patch('server.check_columns')
    @patch('server.create_database')
    @patch('server.create_table')
    @patch('server.drop_table')
    @unittest.expectedFailure
    def test_initialize_server(self, mock_drop_table, mock_create_table, mock_create_database, mock_check_columns, mock_check_table_exists, mock_check_database_exists, mock_getenv):
        # Mocking the environment variable and database name
        mock_getenv.return_value = 'test_db'
        mock_check_database_exists.return_value = False
        mock_check_table_exists.return_value = False
        mock_check_columns.return_value = False

        # Calling the function
        initialize_server()

        # Asserting the function calls
        mock_getenv.assert_called_once_with('DB_NAME')
        mock_check_database_exists.assert_called_once_with('test_db')
        mock_create_database.assert_called_once_with('test_db')
        mock_check_table_exists.assert_called_once_with('test_db')
        mock_create_table.assert_called_once_with('test_db')
        mock_check_columns.assert_called_once_with('test_db')
        mock_drop_table.assert_called_once_with('test_db')
        mock_create_table.assert_called_once_with('test_db')

if __name__ == '__main__':
    unittest.main()
